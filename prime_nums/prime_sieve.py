'''
CHALLENGE DESCRIPTION:
(https://www.codeeval.com/open_challenges/46/)

Print out the prime numbers less than a given number N. For bonus
points your solution should run in N*(log(N)) time or better. You
may assume that N is always a positive integer.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename.
Each line in this file is one test case. Each test case will contain an
integer n < 4,294,967,295. E.g.
10
20
100

OUTPUT SAMPLE:
For each line of input, print out the prime numbers less than N, in
ascending order, comma delimited. (There should not be any spaces between
the comma and numbers) E.g.
2,3,5,7
2,3,5,7,11,13,17,19
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
'''


from itertools import imap
from string import rstrip
from sys import argv


def primes(up_to):

    all_nums = set(range(2, up_to))
    count = 2

    while count * count < up_to:

        if count in all_nums:
            multiples = range(count * count, up_to, count)
            # print 'removing multiples of', count, multiples
            all_nums.difference_update(multiples)

        count += 1

    return sorted(all_nums)

with open(argv[1]) as input_file:
    numbers = filter(lambda num: num, imap(rstrip, input_file))

for num in numbers:
    num = int(num)
    print ','.join(imap(str, primes(num)))
