"""
Module to remove redundant char in string
"""

import sys

if len(sys.argv) == 2:
    res_str = sys.argv[1][0]
    if len(sys.argv[1]) > 1:
        pre_letter = res_str
        for letter in sys.argv[1][1:]:
            if pre_letter != letter:
                res_str += letter
            pre_letter = letter
    print(res_str)

else:
    print('error.')
