"""Core functionality for SEG-Y ninja templates."""
from abc import abstractmethod
from typing import Any
from typing import Optional

import numpy as np
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic.alias_generators import to_camel


class CamelCaseModel(BaseModel):
    """Base model with camel case aliases. Extends BaseModel.

    Attributes:
        model_config: The configuration dictionary for the model.
            - alias_generator: The function used to generate aliases.
            - populate_by_name: Flag indicating whether to populate by name.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    def model_dump(self, *args: Any, **kwargs: Any) -> dict[str, Any]:  # noqa: ANN401
        """Dump the model into a dictionary by alias."""
        return super().model_dump(
            *args, **kwargs, by_alias=True, exclude_defaults=True, exclude_unset=True
        )

    def model_dump_json(self, *args: Any, **kwargs: Any) -> str:  # noqa: ANN401
        """Dump the model into a JSON string by alias."""
        return super().model_dump_json(
            *args, **kwargs, by_alias=True, exclude_defaults=True, exclude_unset=True
        )


class BaseTypeDescriptor(CamelCaseModel):
    """A base model for all SEG-Y Ninja types."""

    description: Optional[str] = Field(
        default=None, description="Description of the field."
    )

    @property
    @abstractmethod
    def dtype(self) -> np.dtype:
        """A conversion routine to numpy data type."""

    @property
    def itemsize(self) -> int:
        """Number of bytes for the data type."""
        return self.dtype.itemsize
