#!/usr/bin/env python3
"""optional annotation"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ tuple with optional types
    """
    return (k, float(v**2))
