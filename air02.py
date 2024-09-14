"""
Module to join a string array into one array separated by a separator given in argument
"""

import sys

def concat(array, _separator):
    """
    Concat string of array separated by a separator
    """
    return _separator.join(array)

if len(sys.argv) > 2:
    separator = sys.argv[-1]
    del sys.argv[-1]
    del sys.argv[0]

    string = concat(sys.argv, separator)
    print(string)
else:
    print('error.')
