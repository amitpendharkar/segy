"""Implements a registry for various SEG-Y standards."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from segy.schema.segy import SegyDescriptor
    from segy.schema.segy import SegyStandard

registry = {}


def register_spec(spec_type: SegyStandard, spec: SegyDescriptor) -> None:
    """Register a SEG-Y standard with its descriptor."""
    registry[spec_type] = spec


def get_spec(spec_type: SegyStandard) -> SegyDescriptor:
    """Get a registered SEG-Y standard's descriptor."""
    spec = registry.get(spec_type)

    if spec is None:
        msg = (
            f"Unknown or unsupported SEG-Y spec: {spec_type}. If you "
            f"would like to use {spec_type}, please register it with "
            f"the `SegySpecFactory` using its `register_spec` method."
        )
        raise NotImplementedError(msg)

    return spec.model_copy(deep=True)
