#!/usr/bin/env python3
"""medaly max module"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait max_delay with random delay and reurns
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
