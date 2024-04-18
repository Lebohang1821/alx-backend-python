#!/usr/bin/env python3
'''A type-annotated function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''It makes multiplier function
    '''
    return lambda x: x * multiplier
