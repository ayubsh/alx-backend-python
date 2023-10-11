#!/usr/bin/env python3
"""generator random numbs"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """generate random 10 numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
