"""
Module to display content of a file like cat
"""

import sys

if len(sys.argv) == 2:
    try:
        file = open(sys.argv[1], 'r', encoding="utf-8")
        line = file.readline()
        res_str = ''
        while line:
            res_str += line
            line = file.readline()
        print(res_str)
        file.close()
    except FileNotFoundError:
        print('bad file')
        sys.exit(1)
else:
    print('error')
