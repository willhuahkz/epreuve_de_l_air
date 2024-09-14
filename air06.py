"""
Module return string that don't containe another string
"""

import sys

def compare_array_str(array_str_, verification_str_):
    """
    Return string of string that don't contain str
    """
    res = []
    for str_ in array_str_:
        if not verification_str_ in str_.lower():
            res.append(str_)
    return ' '.join(res)

if len(sys.argv) > 2:
    verification_str = sys.argv[-1]
    array_str = sys.argv[1:-1]
    print(compare_array_str(array_str, verification_str))
else:
    print('error.')
