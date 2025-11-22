"""Academate college helper package."""

from __future__ import annotations

import sys
import types as _std_types

# Python 3.9 compatibility patch: add ``UnionType`` if it is missing
if sys.version_info < (3, 10) and not hasattr(_std_types, "UnionType"):
	_std_types.UnionType = type(type(None))  # type: ignore[attr-defined]

__all__ = []
__version__ = "1.0.0"
