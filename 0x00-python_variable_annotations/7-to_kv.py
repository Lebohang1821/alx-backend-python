#!/usr/bin/env python3
'''The omplex types - string and int/float tuple
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''It converts key and its value to tuple of key and
    square of its value
    '''
    return (k, float(v**2))
