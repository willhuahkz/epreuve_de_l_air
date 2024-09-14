"""
Module to print a stair of char
"""

import sys

def get_stair(symbol, nb_stage):
    """
    Return the stair
    """
    stair = []
    nb_symbol = nb_stage * 2 - 1
    space = 0
    for i in range(nb_stage, 0, -1):
        string = ' ' * int(space / 2)
        string += symbol * (nb_symbol - space)
        string += ' ' * int(space / 2)
        space += 2
        stair.append(string)
    return stair

if len(sys.argv) == 3:
    if len(sys.argv[1]) == 1:
        try:
            _symbol = sys.argv[1]
            number = int(sys.argv[2])
            if number < 1:
                print('error, number should > 0')
                sys.exit(1)
            _stair = get_stair(_symbol, number)
            for i in range(len(_stair) -1, -1, -1):
                print(_stair[i])
            sys.exit(0)
        except ValueError:
            print('error. nb of stage should a digit')

print('error')
