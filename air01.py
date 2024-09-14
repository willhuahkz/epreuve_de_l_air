"""
Split a string given by a seprator
"""

import sys

def split(_string, separator):
    """
    Split a string via a separator
    """
    res = []
    index = 0
    word = ''
    while 1:
        try:
            index = _string.index(separator)
            word = _string[:index]
            res.append(word)
            _string = _string[index + len(separator):]
        except ValueError:
            res.append(_string)
            return res
    return res

if __name__ == '__main__':
    if len(sys.argv) == 3:
        array = split(sys.argv[1], sys.argv[2])
        for word in array:
            print(word)
    else:
        print('error.')
