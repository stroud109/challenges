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

from itertools import imap
from string import rstrip
from sys import argv


def fibonacci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_list(n):
    new_list = []
    if n == 0:
        return n
    else:
        while n:
            new_list.append(fibonacci(n))
            n = n - 1
        return new_list[0]

with open(argv[1]) as input_file:
    input_nums = filter(lambda num: num, imap(rstrip, input_file))

for num in input_nums:
    print fib_list(int(num))

