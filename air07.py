"""
Module to insert a value in a sorted list
"""

import sys

def is_sorted(_array):
    """
    Verify if an array is sorted
    """
    for i in range(len(_array) - 1):
        if _array[i] > _array[i + 1]:
            return False
    return True

def sorted_array(_array, new_element):
    """
    Insert a value and return the sorted array
    """
    for i, number in enumerate(_array):
        if new_element < number:
            res_array = []
            res_array = _array[:i]
            res_array.append(new_element)
            res_array += _array[i:len(_array)]
            return res_array
    # already sorted
    _array.append(new_element)
    return _array

if __name__ == '__main__':
    if len(sys.argv) > 2:
        try:
            value_to_insert = int(sys.argv[-1])
            array = [int(arg) for arg in sys.argv[1:-1]]
        except ValueError:
            print('error: arguments should be only digit')
            sys.exit(1)
        if not is_sorted(array):
            print('List must be sorted')
            sys.exit(1)
        else:
            res = sorted_array(array, value_to_insert)
            res_str = ' '.join(str(element) for element in res)
            print(res_str)

    else:
        print('error.')
