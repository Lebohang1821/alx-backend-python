#!/usr/bin/env python3
'''function’s parameters and returns values
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Length of list of sequences
    '''
    return [(i, len(i)) for i in lst]
