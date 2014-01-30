'''
Stack Implementation
(https://www.codeeval.com/open_challenges/9/)

CHALLENGE DESCRIPTION:
Write a program implementing a stack inteface for integers.
The interface should have 'push' and 'pop' functions. You
will be asked to 'push' a series of integers and then 'pop'
and print out every alternate integer.

INPUT SAMPLE:
Your program should accept as its first argument a path to
a filename containing a series of space delimited integers,
one per line. E.g.

1 2 3 4
10 -2 3 4

OUTPUT SAMPLE:
Print to stdout, every alternate integer(space delimited),
one per line. E.g.

4 2
4 -2
'''

import re
from sys import argv

solution_file = open(argv[1])
solution_list = solution_file.readlines()


def implement_stack(num_list):
    num_list = num_list.split(' ')
    stack_output = []

    for n in range(len(num_list)):
        if len(num_list) == 1:
            stack_output.append(num_list.pop())

        while len(num_list) > 1:
            stack_output.append(num_list.pop())
            num_list.pop()

    print ' '.join(stack_output)

for row in solution_list:
    row = re.sub(' +', ' ', row)
    row = row.strip()
    if row:
        implement_stack(row)
