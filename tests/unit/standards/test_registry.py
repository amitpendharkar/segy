"""tests for functions in segy.schema.registry."""
import pytest

from segy.schema import SegyDescriptor
from segy.standards import SegyStandard
from segy.standards import rev0_segy
from segy.standards import rev1_segy
from segy.standards.registry import get_spec


@pytest.mark.parametrize(
    ("standard_enum", "base_spec"),
    [(SegyStandard.REV0, rev0_segy), (SegyStandard.REV1, rev1_segy)],
)
def test_get_spec(standard_enum: SegyStandard, base_spec: SegyDescriptor) -> None:
    """Test retrieving SegyStandard from registry.

    Args:
        standard_enum (SegyStandard): the SegyStandard to get
        base_spec (SegyDescriptor): the SegyDescriptor for comparison
    """
    spec_copy = get_spec(SegyStandard(standard_enum))
    assert spec_copy == base_spec
    assert id(spec_copy) != id(base_spec)
