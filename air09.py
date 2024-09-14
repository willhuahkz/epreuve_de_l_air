"""
Module to rotate at left every element of an array
"""

import sys

def rotate_left(array):
    """
    Move to the left every element of the array
    """
    res = []
    for element in array[1:]:
        res.append(element)
    res.append(array[0])
    return res

if len(sys.argv) > 1:
    arguments = sys.argv[1:]
    res_str = ' '.join(rotate_left(arguments))
    print(res_str)

else:
    print('error.')
