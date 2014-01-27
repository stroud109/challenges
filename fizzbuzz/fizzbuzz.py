'''
Fizzbuzz

INPUT SAMPLE:

Your program should read an input file (provided on the command line)
which contains multiple newline separated lines. Each line will contain
3 numbers which are space delimited. The first number is first number to
divide by ('A' in this example), the second number is the second number
to divide by ('B' in this example) and the third number is where you
should count till ('N' in this example). You may assume that the input
file is formatted correctly and is the numbers are valid positive
integers. E.g.

3 5 10
2 7 15

OUTPUT SAMPLE:

Print out the series 1 through N replacing numbers divisible by 'A' by
F, numbers divisible by 'B' by B and numbers divisible by both as 'FB'.
Since the input file contains multiple sets of values, your output will
print out one line per set. Ensure that there are no trailing empty spaces
on each line you print. E.g.

1 2 F 4 B F 7 8 F B
1 F 3 F 5 F B F 9 F 11 F 13 FB 15
'''

import re
from sys import argv

solution_file = open(argv[1])
num_sequence = solution_file.readlines()


def fizzbuzz(num_sequence):

    num_sequence = re.sub(' +', ' ', num_sequence)
    num_sequence = num_sequence.strip()

    if num_sequence:

        split_nums = num_sequence.split(' ')
        fizz = int(split_nums[0])
        buzz = int(split_nums[1])
        max_num = int(split_nums[2]) + 1
        solution = ''

        for num in range(max_num):
            if num > 0:
                if num % fizz == 0 and num % buzz == 0:
                    solution += 'FB '
                elif num % fizz == 0:
                    solution += 'F '
                elif num % buzz == 0:
                    solution += 'B '
                else:
                    solution += str(num) + ' '
        solution = re.sub(' +', ' ', solution)
        solution = solution.strip()
        print solution

for sequence in num_sequence:
        fizzbuzz(sequence)
