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


def primes(num):

    list_of_primes = [2]
    counter = 3

    # We're going to continue finding primes using our counter
    # until we break out of it when our counter's value exceeds
    # the target num.
    while True:

        is_prime = True

        for prime in list_of_primes:

            if counter % prime == 0:
                is_prime = False
                break

        if is_prime:

            # If the counter is greater than our target num, then we're
            # done and we can break the while loop and return the list.
            if counter > num:
                break

            list_of_primes.append(counter)

        counter += 1

    return list_of_primes


with open(argv[1]) as input_file:
    numbers = filter(lambda num: num, imap(rstrip, input_file))

for num in numbers:
    num = int(num)
    print ','.join(imap(str, primes(num)))
