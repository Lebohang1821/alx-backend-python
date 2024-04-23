#!/usr/bin/env python3
'''It imports async_comprehension from previous file'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''It executes imported function four times asynchronously
    and measures total execution time'''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
