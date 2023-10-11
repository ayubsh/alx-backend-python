#!/usr/bin/env python3
"""async comprehence"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns list of async floats
    """
    return [i async for i in async_generator()]
