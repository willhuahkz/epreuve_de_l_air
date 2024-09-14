"""
Module to add an addition or substraction to every element of a list
"""

import sys
import re

if len(sys.argv) > 2:
    PATTERN = r'(\+|-)\d'
    if re.match(PATTERN, sys.argv[-1]):
        operator = sys.argv[-1][0]
        operator_number = int(sys.argv[-1][1:])
        # if before for because of optimisation
        try:
            array_number = [int(arg) for arg in sys.argv[1:-1]]
            if operator == '+':
                array_number = [number + operator_number for number in array_number]
            else:
                array_number = [number - operator_number for number in array_number]
            res_str = ' '.join(str(number) for number in array_number)
            print(res_str)
        except ValueError:
            print('error: arguments should be only digits')
    else:
        print('error: operator(+ | -) + digit')
else:
    print('error.')
