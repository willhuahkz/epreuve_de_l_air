"""
Module to test exercises of air
"""

import sys
import subprocess

def print_red(string):
    """
    Print in red
    """
    print(f'❌ \033[91m{string}\033[0m')

def print_green(string):
    """
    Print in green
    """
    print(f'✅ \033[92m{string}\033[0m')

def verify_files():
    """
    Verify if repository contains every files
    """
    for i in range(12):
        try:
            file_to_open = f'air{i:02}.py'
            file = open(file_to_open, 'r', encoding="utf-8")
            file.close()
        except FileNotFoundError:
            print_red(f'Error: file {file_to_open} not found')
            sys.exit(1)
    print_green('Files found')

def run_test(exercise, expected_output, current_test, max_test, args=None):
    """
    Run a test
    """
    if args is None:
        args = []
    exercise_name = f'air{exercise:02}.py'
    result = subprocess.run(['python3', exercise_name] + args, capture_output=True, text=True, check=False)
    if result.stdout != expected_output:
        print_red(f'Error:\Excepted: {expected_output}\nGot: {result.stdout}')
    else:
        print_green(f'Success: {exercise_name} ({current_test}/{max_test})')

verify_files()


run_test(0, 'a\nb\nc\n', 1, 1, ['a b c'])
run_test(1, 'Crevette magique dans \n mer des étoiles\n', 1, 1, ['Crevette magique dans la mer des étoiles', 'la'])
run_test(2, 'a b c\n', 1, 1, ['a', 'b', 'c', ' '])
run_test(3, '5\n', 1, 1, ['1', '2', '3', '4', '5', '4', '3', '2', '1'])
run_test(4, 'Helo milady, bien ou quoi ?\n', 1, 1, ['Hello milady,   bien ou quoi ??'])
run_test(5, '3 4 5 6 7\n', 1, 1, ['1', '2', '3', '4', '5', '+2'])
run_test(6, 'Michel\n', 1, 1, ['Michel', 'Albert', 'Thérèse', 'Benoit', 't'])
run_test(7, '1 2 3 4\n', 1, 1, ['1', '3', '4', '2'])
run_test(8, '10 15 20 25 30 35\n', 1, 1, ['10', '20', '30', 'fusion', '15', '25', '35'])
run_test(9, 'Albert, Thérèse, Benoit, Michel\n', 1, 1, ['Michel', 'Albert', 'Thérèse', 'Benoit'])
run_test(10, 'hello world\n\n', 1, 1, ['a.txt'])
run_test(11,
"""    o    
   ooo   
  ooooo  
 ooooooo 
ooooooooo
""",
1,1, ['o', '5']
)
run_test(12, '1 2 3 4 5 6\n', 1, 1, ['6', '5', '4', '3', '2', '1'])
