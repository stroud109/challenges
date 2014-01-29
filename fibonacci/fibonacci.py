'''
Fibonacci
(https://www.codeeval.com/open_challenges/22/)

CHALLENGE DESCRIPTION:
The Fibonacci series is defined as:
F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n>1.
Given a positive integer 'n', print out the F(n).

INPUT SAMPLE:
The first argument will be a path to a filename containing
a positive integer, one per line. E.g.
5
12

OUTPUT SAMPLE:
Print to stdout, the fibonacci number, F(n). E.g.
5
144
'''

import re
from sys import argv

num_file = open(argv[1])
solutions = num_file.readlines()


def fibonacci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_list(n):
    # print "n: ", n
    new_list = []
    if n == 0:
        print n
    else:
        while n:
            new_list.append(fibonacci(n))
            n = n - 1
        print new_list[0]

for num in solutions:
    num = re.sub(' +', ' ', num)
    num = num.strip()
    if num:
        fib_list(int(num))

