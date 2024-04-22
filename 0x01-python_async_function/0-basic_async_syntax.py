#!/usr/bin/env python3
'''basics of async'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''It waits for random amount of time and
    then returns duration of wait
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
