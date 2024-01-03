"""Indexers for SEG-Y files."""


from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Optional

import numpy as np
from fsspec import AbstractFileSystem
from fsspec.utils import merge_offset_ranges
from numpy.typing import NDArray
from pandas import DataFrame

from segy.ibm import ibm2ieee
from segy.schema import ScalarType
from segy.schema import TraceDescriptor
from segy.schema.data_type import StructuredDataTypeDescriptor


def trace_ibm2ieee_inplace(trace: NDArray[Any]) -> NDArray[Any]:
    """Convert data of a trace (headers + data) from IBM32 to float32 in place.

    Args:
        trace: A numpy array of type <trace-dtype> containing the trace data.

    Returns:
        A numpy array of type <new-trace-dtype> converted from the input trace data,
        preserving the original header information.

    Note:
        This method converts IBM format trace data to IEEE format inplace, without
        creating a copy of the trace array.
    """
    header_dtype = trace.dtype["header"]
    data_dtype = trace.dtype["data"]

    num_samp = data_dtype.shape
    data_dtype_f32 = np.dtype(("float32", num_samp))

    trace_dtype_fp32 = np.dtype([("header", header_dtype), ("data", data_dtype_f32)])
    trace["data"] = ibm2ieee(trace["data"]).view("uint32")

    return trace.view(trace_dtype_fp32)


def merge_cat_file(
    fs: AbstractFileSystem,
    url: str,
    starts: list[int],
    ends: list[int],
    block_size: int = 8_388_608,
) -> bytearray:
    """Merge sequential byte start/ends and fetch from store.

    Args:
        fs: fsspec FileSystem instance.
        url: Path/URL to file.
        starts: List of start byte locations.
        ends: List of end byte locations.
        block_size: Optional, block size for concurrent downloads.
            Default is 8MiB.

    Returns:
        Bytearray containing all the requested data.
    """
    paths = [url] * len(starts)

    paths, starts, ends = merge_offset_ranges(
        paths,
        starts,
        ends,
        max_block=block_size,
        sort=True,
    )

    buffer_bytes = fs.cat_ranges(
        paths=paths,
        starts=starts,
        ends=ends,
    )

    return bytearray(b"".join(buffer_bytes))


def bounds_check(indices: list[int], max_: int, type_: str) -> None:
    """Check if indices are out of bounds (negative, or more than max).

    Wrapping negative indices is not supported yet. The `type_` argument
    will be used in exceptions to be descriptive.

    Args:
        indices: A list of integer indices.
        max_: The maximum value of the index range.
        type_: The type of indices being checked.

    Raises:
        IndexError: If any of the indices are negative or exceed the maximum value.
    """
    negative_indices = [index for index in indices if index < 0]
    out_of_range_indices = [index for index in indices if index >= max_]

    outliers = negative_indices + out_of_range_indices

    if outliers:
        msg = (
            f"Requested {type_} indices {outliers} are out of bounds. SEG-Y "
            f"file has {max_} traces. Valid indices are "
            f"[0, {max_ - 1})."
        )
        raise IndexError(msg)


class AbstractIndexer(ABC):
    """Abstract class for indexing and fetching structured data from a remote file.

    We calculate byte ranges from indexing of SEG-Y components and use them
    to fetch the data and decode it.

    Args:
        fs: An instance of `fsspec` file-system.
        url: A string representing the URL of the file.
        spec: An instance of StructuredDataTypeDescriptor.
        max_value: An integer representing the maximum value of the index.
        kind: A string representing the kind of index.
        postprocess_kwargs: Optional dictionary representing additional arguments
            for post-processing.
    """

    def __init__(  # noqa: PLR0913
        self,
        fs: AbstractFileSystem,
        url: str,
        spec: StructuredDataTypeDescriptor,
        max_value: int,
        kind: str,
        postprocess_kwargs: Optional[dict[str, Any]] = None,
    ):
        """Initialize indexer for a FileSystem and a file with given spec."""
        self.fs = fs
        self.url = url
        self.spec = spec
        self.max_value = max_value
        self.kind = kind
        self.postprocess_kwargs = postprocess_kwargs

    @abstractmethod
    def indices_to_byte_ranges(self, indices: list[int]) -> tuple[list[int], list[int]]:
        """Logic to calculate start/end bytes."""

    @abstractmethod
    def decode(self, buffer: bytearray) -> NDArray[Any]:
        """How to decode the bytes after reading."""

    def __getitem__(self, item: int | list[int] | slice) -> Any:  # noqa: ANN401
        """Operator for integers, lists, and slices with bounds checking."""
        if isinstance(item, int):
            indices = [item]
            bounds_check(indices, self.max_value, self.kind)

        elif isinstance(item, list):
            indices = item
            bounds_check(indices, self.max_value, self.kind)

        elif isinstance(item, slice):
            if item.step == 0:
                msg = "Step of 0 is invalid for slicing."
                raise ValueError(msg)

            start = item.start or 0
            stop = item.stop or self.max_value

            bounds_check([start, stop - 1], self.max_value, self.kind)
            indices = list(range(*item.indices(self.max_value)))

        else:
            msg = f"Invalid index type {type(item)}"
            raise TypeError(msg)

        data = self.fetch(indices)
        return self.post_process(data)

    def post_process(self, data: NDArray[Any]) -> Any:  # noqa: ANN401
        """Optional post-processing. Override in subclass if needed."""
        return data

    def fetch(self, indices: list[int]) -> NDArray[Any]:
        """Fetches and decodes binary data from the given indices.

        Args:
            indices: A list of integers representing the indices.

        Returns:
            An NDArray of any type representing the fetched data.

        Note:
            - This method internally converts the indices to byte ranges using
                the 'indices_to_byte_ranges' method.
            - The byte ranges are used to fetch the corresponding data from the
                file specified by the 'url' parameter.
            - The fetched data is then decoded and squeezed before being returned.
        """
        starts, ends = self.indices_to_byte_ranges(indices)
        buffer = merge_cat_file(self.fs, self.url, starts, ends)
        return self.decode(buffer).squeeze()


class TraceIndexer(AbstractIndexer):
    """Indexer for reading traces (headers + data).

    Inherits from AbstractIndexer. Implements decoding based on trace
    descriptor. It will optionally return the headers as a Pandas
    DataFrame.
    """

    spec: TraceDescriptor

    def indices_to_byte_ranges(self, indices: list[int]) -> tuple[list[int], list[int]]:
        """Convert trace indices to byte ranges."""
        start_offset = self.spec.offset
        trace_itemsize = self.spec.dtype.itemsize

        starts = [start_offset + i * trace_itemsize for i in indices]
        ends = [start + trace_itemsize for start in starts]

        return starts, ends

    def decode(self, buffer: bytearray) -> NDArray[Any]:
        """Decode whole traces (header + data)."""
        data = np.frombuffer(buffer, dtype=self.spec.dtype)

        # TODO(Altay): Handle little endian.
        data = data.byteswap(inplace=True).newbyteorder()

        if self.spec.data_descriptor.format == ScalarType.IBM32:
            data = trace_ibm2ieee_inplace(data)

        return data

    def post_process(
        self, data: NDArray[Any]
    ) -> NDArray[Any] | dict[str, NDArray[Any] | DataFrame]:
        """Either return struct array or (Header) DataFrame + (Data) Array."""
        using_pandas = self.postprocess_kwargs.get("pandas_headers", False)
        if using_pandas:
            return {"header": DataFrame(data["header"]), "data": data["data"]}

        return data


class HeaderIndexer(AbstractIndexer):
    """Indexer for reading trace headers only.

    Inherits from AbstractIndexer. Implements decoding based on trace
    descriptor. It will optionally return the headers as a Pandas
    DataFrame.
    """

    spec: TraceDescriptor

    def indices_to_byte_ranges(self, indices: list[int]) -> tuple[list[int], list[int]]:
        """Convert header indices to byte ranges (without trace data)."""
        trace_itemsize = self.spec.dtype.itemsize
        header_itemsize = self.spec.header_descriptor.itemsize

        start_offset = self.spec.offset

        starts = [start_offset + i * trace_itemsize for i in indices]
        ends = [start + header_itemsize for start in starts]

        return starts, ends

    def decode(self, buffer: bytearray) -> NDArray[Any]:
        """Decode headers only."""
        data = np.frombuffer(buffer, dtype=self.spec.header_descriptor.dtype)

        # TODO(Altay): Handle little endian.
        # TODO(Altay): Handle float/ibm32 etc headers.
        data = data.byteswap(inplace=True).newbyteorder()

        return data  # noqa: RET504

    def post_process(self, data: NDArray[Any]) -> NDArray[Any] | DataFrame:
        """Either return header as struct array or DataFrame."""
        using_pandas = self.postprocess_kwargs.get("pandas_headers", False)
        if using_pandas:
            return DataFrame(data)

        return data


class DataIndexer(AbstractIndexer):
    """Indexer for reading trace data only.

    Inherits from AbstractIndexer. Implements decoding based on trace
    descriptor.
    """

    spec: TraceDescriptor

    def indices_to_byte_ranges(self, indices: list[int]) -> tuple[list[int], list[int]]:
        """Convert data indices to byte ranges (without trace headers)."""
        trace_itemsize = self.spec.dtype.itemsize
        data_itemsize = self.spec.data_descriptor.dtype.itemsize
        header_itemsize = self.spec.header_descriptor.dtype.itemsize

        start_offset = self.spec.offset + header_itemsize

        starts = [start_offset + i * trace_itemsize for i in indices]
        ends = [start + data_itemsize for start in starts]

        return starts, ends

    def decode(self, buffer: bytearray) -> NDArray[Any]:
        """Decode trace data only."""
        data = np.frombuffer(buffer, dtype=self.spec.data_descriptor.dtype)

        # TODO(Altay): Handle little endian.
        data = data.byteswap(inplace=True).newbyteorder()

        if self.spec.data_descriptor.format == ScalarType.IBM32:
            data = ibm2ieee(data).view("float32")

        return data