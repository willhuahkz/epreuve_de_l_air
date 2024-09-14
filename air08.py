"""
Module to fetch two list of int
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


def bubble_sort(array_to_sort):
    """
    Bubble sort
    """
    while not is_sorted(array_to_sort):
        for i in range(len(array_to_sort) - 1):
            if array_to_sort[i] > array_to_sort[i + 1]:
                tmp = array_to_sort[i + 1]
                array_to_sort[i + 1] = array_to_sort[i]
                array_to_sort[i] = tmp
    return array_to_sort

def sorted_fusion(array1, array2):
    """
    Fetch two arrays in order
    """
    i = 0
    j = 0
    res = []
    size = len(array1) + len(array2)
    while len(res) < size:
        if (
            j >= len(array2)
            or i < len(array1) and array1[i] < array2[j]
        ):
            res.append(array1[i])
            i += 1
        else:
            res.append(array2[j])
            j += 1
    return res

if len(sys.argv) > 3:
    try:
        arguments = sys.argv[1:]
        index = arguments.index('fusion')
        if index == 0 or index == len(arguments) - 1:
            print('error. Fusion placement')
            sys.exit(1)

        first_array = [int(arg) for arg in arguments[:index]]
        second_array = [int(arg) for arg in arguments[index + 1:len(arguments)]]
        res = sorted_fusion(bubble_sort(first_array), bubble_sort(second_array))
        res_str = ' '.join([str(nb) for nb in res]) 
        print(res_str)
    except ValueError:
        print('error. Bad usage')

else:
    print('error.')
