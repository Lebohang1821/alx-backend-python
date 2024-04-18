#!/usr/bin/env python3
'''The basic annotations - floor
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''It retrieves first element of sequence if it exists
    '''
    if lst:
        return lst[0]
    else:
        return None
