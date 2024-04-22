#!/usr/bin/env python3
'''It imports wait_random from 0-basic_async_syntax'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''It creates asynchronous task - wait random'''
    return asyncio.create_task(wait_random(max_delay))
