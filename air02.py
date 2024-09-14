"""
Module to join a string array into one array separated by a separator given in argument
"""

import sys

if len(sys.argv) > 2:
    separator = sys.argv[-1]
    del sys.argv[-1]
    del sys.argv[0]
    string = separator.join(sys.argv)
    print(string)
else:
    print('error.')
