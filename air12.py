"""
Module to sort a list by using quick sort
"""

import sys

from air07 import is_sorted

def quick_sort(array):
    """
    Sort an array by quick sort algorithm
    """
    if len(array) <= 1:
        return array
    pivot = array.pop()
    left = []
    right = [pivot]

    for number in array:
        if number <= pivot:
            left.append(number)
        else:
            right.append(number)

    return quick_sort(left) + quick_sort(right)

if len(sys.argv) > 1:
    _array = sys.argv[1:]
    try:
        _array_int = [int(num) for num in _array]
        _array_sorted = quick_sort(_array_int)
        _string = ' '.join(str(number) for number in _array_sorted)
        print(_string)
    except ValueError:
        print('error: only number allowed')

else:
    print('error.')
