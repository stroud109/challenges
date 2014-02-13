'''
N MOD M
(https://www.codeeval.com/open_challenges/62/)

CHALLENGE DESCRIPTION:
Given two integers N and M, calculate N Mod M (without using any inbuilt
 modulus operator).

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each
line in this file contains two comma separated positive integers. E.g.
20,6
2,3

You may assume M will never be zero.
'''

from itertools import imap
from string import rstrip
from sys import argv


def mod(n, m):
    # print 'n: ', n
    # print 'm: ', m
    if n == m:
        return 0
    elif m > n:
        return n
    else:
        # `i` signifies how many times `m` can cleanly fit into `n`.
        # Using an int rather than a float will give us this value.
        i = n / m
        # print '%d / % d = %d' % (n, m, i)
        # print '%d - (%d * %d)' % (n, i, m)
        return n - (i * m)


with open(argv[1]) as input_file:
    lines = filter(lambda line: line, imap(rstrip, input_file))

for line in lines:
    n, m = line.split(',')
    n = int(n)
    m = int(m)
    print mod(n, m)
