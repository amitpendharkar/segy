"""SEG-Y Revision 0 Specification."""

from segy.schema import Endianness
from segy.schema import ScalarType
from segy.schema import SegyDescriptor
from segy.schema import SegyStandard
from segy.schema import TextHeaderDescriptor
from segy.schema import TextHeaderEncoding
from segy.schema import TraceDataDescriptor
from segy.schema import TraceDescriptor
from segy.schema.data_type import StructuredDataTypeDescriptor
from segy.schema.data_type import StructuredFieldDescriptor

BINARY_FILE_HEADER_FIELDS_REV0 = [
    StructuredFieldDescriptor(
        name="job_id",
        offset=0,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Job Identification Number",
    ),
    StructuredFieldDescriptor(
        name="line_no",
        offset=4,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Line Number",
    ),
    StructuredFieldDescriptor(
        name="reel_no",
        offset=8,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Reel Number",
    ),
    StructuredFieldDescriptor(
        name="data_traces_ensemble",
        offset=12,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Number of Data Traces per Ensemble",
    ),
    StructuredFieldDescriptor(
        name="aux_traces_ensemble",
        offset=14,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Number of Auxiliary Traces per Ensemble",
    ),
    StructuredFieldDescriptor(
        name="sample_interval",
        offset=16,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sample Interval",
    ),
    StructuredFieldDescriptor(
        name="sample_interval_orig",
        offset=18,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sample Interval of Original Field Recording",
    ),
    StructuredFieldDescriptor(
        name="samples_per_trace",
        offset=20,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Number of Samples per Data Trace",
    ),
    StructuredFieldDescriptor(
        name="samples_per_trace_orig",
        offset=22,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Number of Samples per Data Trace for Original Field Recording",
    ),
    StructuredFieldDescriptor(
        name="data_sample_format",
        offset=24,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Data Sample Format Code",
    ),
    StructuredFieldDescriptor(
        name="ensemble_fold",
        offset=26,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Ensemble Fold",
    ),
    StructuredFieldDescriptor(
        name="trace_sorting",
        offset=28,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Trace Sorting Code",
    ),
    StructuredFieldDescriptor(
        name="vertical_sum",
        offset=30,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Vertical Sum Code",
    ),
    StructuredFieldDescriptor(
        name="sweep_freq_start",
        offset=32,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Frequency at Start",
    ),
    StructuredFieldDescriptor(
        name="sweep_freq_end",
        offset=34,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Frequency at End",
    ),
    StructuredFieldDescriptor(
        name="sweep_length",
        offset=36,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Length",
    ),
    StructuredFieldDescriptor(
        name="sweep_type",
        offset=38,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Type Code",
    ),
    StructuredFieldDescriptor(
        name="sweep_trace_no",
        offset=40,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Trace Number of Sweep Channel",
    ),
    StructuredFieldDescriptor(
        name="sweep_taper_start",
        offset=42,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Trace Taper Length at Start",
    ),
    StructuredFieldDescriptor(
        name="sweep_taper_end",
        offset=44,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Trace Taper Length at End",
    ),
    StructuredFieldDescriptor(
        name="taper_type",
        offset=46,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Taper Type",
    ),
    StructuredFieldDescriptor(
        name="correlated_traces",
        offset=48,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Correlated Data Traces",
    ),
    StructuredFieldDescriptor(
        name="binary_gain",
        offset=50,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Binary Gain Recovered",
    ),
    StructuredFieldDescriptor(
        name="amp_recovery_method",
        offset=52,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Amplitude Recovery Method",
    ),
    StructuredFieldDescriptor(
        name="measurement_system",
        offset=54,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Measurement System",
    ),
    StructuredFieldDescriptor(
        name="impulse_signal_polarity",
        offset=56,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Impulse Signal Polarity",
    ),
    StructuredFieldDescriptor(
        name="vibratory_polarity",
        offset=58,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Vibratory Polarity Code",
    ),
]


TRACE_HEADER_FIELDS_REV0 = [
    StructuredFieldDescriptor(
        name="trace_seq_line",
        offset=0,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Trace Sequence Number within Line",
    ),
    StructuredFieldDescriptor(
        name="trace_seq_file",
        offset=4,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Trace Sequence Number within File",
    ),
    StructuredFieldDescriptor(
        name="field_rec_no",
        offset=8,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Original Field Record Number",
    ),
    StructuredFieldDescriptor(
        name="trace_no_field_rec",
        offset=12,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Trace Number within the Field Record",
    ),
    StructuredFieldDescriptor(
        name="energy_src_pt",
        offset=16,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Energy Source Point Number",
    ),
    StructuredFieldDescriptor(
        name="cdp_ens_no",
        offset=20,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Ensemble Number (CDP, CMP, etc.)",
    ),
    StructuredFieldDescriptor(
        name="trace_no_ens",
        offset=24,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Trace Number within the Ensemble",
    ),
    StructuredFieldDescriptor(
        name="trace_id",
        offset=28,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Trace Identification Code",
    ),
    StructuredFieldDescriptor(
        name="vert_sum",
        offset=30,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Number of Vertically Stacked Traces",
    ),
    StructuredFieldDescriptor(
        name="horiz_stack",
        offset=32,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Number of Horizontally Stacked Traces",
    ),
    StructuredFieldDescriptor(
        name="data_use",
        offset=34,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Data Use",
    ),
    StructuredFieldDescriptor(
        name="dist_src_to_rec",
        offset=36,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Distance from Source Point to Receiver Group",
    ),
    StructuredFieldDescriptor(
        name="rec_elev",
        offset=40,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Receiver Group Elevation",
    ),
    StructuredFieldDescriptor(
        name="src_elev",
        offset=44,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Source Elevation",
    ),
    StructuredFieldDescriptor(
        name="src_depth",
        offset=48,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Source Depth",
    ),
    StructuredFieldDescriptor(
        name="datum_elev_rec",
        offset=52,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Datum Elevation at Receiver Group",
    ),
    StructuredFieldDescriptor(
        name="datum_elev_src",
        offset=56,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Datum Elevation at Source",
    ),
    StructuredFieldDescriptor(
        name="water_depth_src",
        offset=60,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Water Depth at Source",
    ),
    StructuredFieldDescriptor(
        name="water_depth_rec",
        offset=64,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Water Depth at Receiver Group",
    ),
    StructuredFieldDescriptor(
        name="scalar_apply_elev",
        offset=68,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Scalar to be applied to all elevations and depths",
    ),
    StructuredFieldDescriptor(
        name="scalar_apply_coords",
        offset=70,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Scalar to be applied to all coordinates",
    ),
    StructuredFieldDescriptor(
        name="src_x",
        offset=72,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Source X coordinate",
    ),
    StructuredFieldDescriptor(
        name="src_y",
        offset=76,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Source Y coordinate",
    ),
    StructuredFieldDescriptor(
        name="rec_x",
        offset=80,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Receiver X coordinate",
    ),
    StructuredFieldDescriptor(
        name="rec_y",
        offset=84,
        format=ScalarType.INT32,
        endianness=Endianness.BIG,
        description="Receiver Y coordinate",
    ),
    StructuredFieldDescriptor(
        name="coord_units",
        offset=88,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Coordinate units",
    ),
    StructuredFieldDescriptor(
        name="weathering_vel",
        offset=90,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Weathering Velocity",
    ),
    StructuredFieldDescriptor(
        name="subweathering_vel",
        offset=92,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Subweathering Velocity",
    ),
    StructuredFieldDescriptor(
        name="uphole_time_src",
        offset=94,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Uphole Time at Source",
    ),
    StructuredFieldDescriptor(
        name="uphole_time_rec",
        offset=96,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Uphole Time at Receiver",
    ),
    StructuredFieldDescriptor(
        name="src_static_corr",
        offset=98,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Source Static Correction",
    ),
    StructuredFieldDescriptor(
        name="rec_static_corr",
        offset=100,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Receiver Static Correction",
    ),
    StructuredFieldDescriptor(
        name="total_static",
        offset=102,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Total Static Applied",
    ),
    StructuredFieldDescriptor(
        name="lag_time_a",
        offset=104,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Lag Time A",
    ),
    StructuredFieldDescriptor(
        name="lag_time_b",
        offset=106,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Lag Time B",
    ),
    StructuredFieldDescriptor(
        name="delay_rec_time",
        offset=108,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Delay Recording Time",
    ),
    StructuredFieldDescriptor(
        name="mute_start",
        offset=110,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Start Time of Mute",
    ),
    StructuredFieldDescriptor(
        name="mute_end",
        offset=112,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="End Time of Mute",
    ),
    StructuredFieldDescriptor(
        name="samples_per_trace",
        offset=114,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Number of Samples in this Trace",
    ),
    StructuredFieldDescriptor(
        name="sample_interval",
        offset=116,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sample Interval for this Trace",
    ),
    StructuredFieldDescriptor(
        name="gain_type",
        offset=118,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Gain Type of Field Instruments",
    ),
    StructuredFieldDescriptor(
        name="instrument_gain",
        offset=120,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Instrument Gain Constant",
    ),
    StructuredFieldDescriptor(
        name="instrument_early_gain",
        offset=122,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Instrument Early Gain",
    ),
    StructuredFieldDescriptor(
        name="correlated",
        offset=124,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Correlated",
    ),
    StructuredFieldDescriptor(
        name="sweep_freq_start",
        offset=126,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Frequency at Start",
    ),
    StructuredFieldDescriptor(
        name="sweep_freq_end",
        offset=128,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Frequency at End",
    ),
    StructuredFieldDescriptor(
        name="sweep_length",
        offset=130,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Length",
    ),
    StructuredFieldDescriptor(
        name="sweep_type",
        offset=132,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Type",
    ),
    StructuredFieldDescriptor(
        name="sweep_trace_taper_start",
        offset=134,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Trace Taper Length at Start",
    ),
    StructuredFieldDescriptor(
        name="sweep_trace_taper_end",
        offset=136,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Sweep Trace Taper Length at End",
    ),
    StructuredFieldDescriptor(
        name="taper_type",
        offset=138,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Taper Type",
    ),
    StructuredFieldDescriptor(
        name="alias_filter_freq",
        offset=140,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Alias Filter Frequency",
    ),
    StructuredFieldDescriptor(
        name="alias_filter_slope",
        offset=142,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Alias Filter Slope",
    ),
    StructuredFieldDescriptor(
        name="notch_filter_freq",
        offset=144,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Notch Filter Frequency",
    ),
    StructuredFieldDescriptor(
        name="notch_filter_slope",
        offset=146,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Notch Filter Slope",
    ),
    StructuredFieldDescriptor(
        name="low_cut_freq",
        offset=148,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Low Cut Frequency",
    ),
    StructuredFieldDescriptor(
        name="high_cut_freq",
        offset=150,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="High Cut Frequency",
    ),
    StructuredFieldDescriptor(
        name="low_cut_slope",
        offset=152,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Low Cut Slope",
    ),
    StructuredFieldDescriptor(
        name="high_cut_slope",
        offset=154,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="High Cut Slope",
    ),
    StructuredFieldDescriptor(
        name="year",
        offset=156,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Year Data Recorded",
    ),
    StructuredFieldDescriptor(
        name="day",
        offset=158,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Day of Year",
    ),
    StructuredFieldDescriptor(
        name="hour",
        offset=160,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Hour of Day",
    ),
    StructuredFieldDescriptor(
        name="minute",
        offset=162,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Minute of Hour",
    ),
    StructuredFieldDescriptor(
        name="second",
        offset=164,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Second of Minute",
    ),
    StructuredFieldDescriptor(
        name="time_basis_code",
        offset=166,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Time Basis Code",
    ),
    StructuredFieldDescriptor(
        name="trace_weighting_factor",
        offset=168,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Trace Weighting Factor",
    ),
    StructuredFieldDescriptor(
        name="geophone_group_no_roll1",
        offset=170,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Geophone Group Number of Roll Switch Position One",
    ),
    StructuredFieldDescriptor(
        name="geophone_group_no_first_trace",
        offset=172,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Geophone Group Number of Trace Number One within Original Field Record",  # noqa: E501
    ),
    StructuredFieldDescriptor(
        name="geophone_group_no_last_trace",
        offset=174,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Geophone Group Number of Last Trace within Original Field Record",  # noqa: E501
    ),
    StructuredFieldDescriptor(
        name="gap_size",
        offset=176,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Gap Size (total number of groups dropped)",
    ),
    StructuredFieldDescriptor(
        name="over_travel",
        offset=178,
        format=ScalarType.INT16,
        endianness=Endianness.BIG,
        description="Over Travel Associated with Taper",
    ),
]


rev0_textual_file_header = TextHeaderDescriptor(
    rows=40,
    cols=80,
    offset=0,
    encoding=TextHeaderEncoding.EBCDIC,
    format=ScalarType.UINT8,  # noqa: A003
)


rev0_binary_file_header = StructuredDataTypeDescriptor(
    fields=BINARY_FILE_HEADER_FIELDS_REV0,
    item_size=400,
    offset=3200,
)


rev0_trace_header = StructuredDataTypeDescriptor(
    fields=TRACE_HEADER_FIELDS_REV0,
    item_size=240,
)


rev0_trace_data = TraceDataDescriptor(
    format=ScalarType.IBM32,  # noqa: A003
    endianness=Endianness.BIG,
)


rev0_trace = TraceDescriptor(
    header_descriptor=rev0_trace_header,
    data_descriptor=rev0_trace_data,
)


rev0_segy = SegyDescriptor(
    segy_standard=SegyStandard.REV0,
    text_file_header=rev0_textual_file_header,
    binary_file_header=rev0_binary_file_header,
    trace=rev0_trace,
)
