#!/usr/bin/env python3
'''Th complex types - list of floats
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''It computs sum of list of integers and floating-point numbers
    '''
    return float(sum(mxd_lst))
