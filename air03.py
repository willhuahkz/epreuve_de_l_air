"""
Module to find an intruder in a string
An intrunder is a string where occurence == 1 of the source string
"""

import sys
from collections import defaultdict

if len(sys.argv) > 2:
    occurences = defaultdict(int)
    for arg in sys.argv[1:]:
        occurences[arg] += 1
    RES_STR = ' '.join([arg for arg in occurences if occurences[arg] == 1])
    print(RES_STR)

else:
    print('error.')
