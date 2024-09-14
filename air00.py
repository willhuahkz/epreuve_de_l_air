"""
Module to split a function by a separator
"""

import sys
import string

def split(_string, separator):
    """
    Split a string via a separator
    """
    res = []
    _word = ''
    for char in _string:
        if char in separator:
            res.append(_word)
            _word = ''
        else:
            _word += char
    # --- [V1] --- #
    # It is if we want that the sepator absolutely match
    # index = 0
    # while 1:
    #     try:
    #         index = _string.index(separator)
    #         word = _string[:index]
    #         res.append(word)
    #         _string = _string[index + len(separator):]
    #     except ValueError:
    #         res.append(_string)
    #         return res
    res.append(_word)
    return res

if len(sys.argv) == 2:
    array = split(sys.argv[1], string.whitespace)
    for word in array:
        print(word)
else:
    print('error.')
