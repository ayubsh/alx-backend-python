#!/usr/bin/env python3
"""iterable obj"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element length
    """
    return [(i, len(i)) for i in lst]
