#!/usr/bin/env python3
"""annotation of function that returna another func"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns func that mult multiplier
    """
    return lambda x: x*multiplier
