'''
LONGEST COMMON SUBSEQUENCE
(https://www.codeeval.com/open_challenges/6/)

CHALLENGE DESCRIPTION:
You are given two sequences. Write a program to determine the longest common
 subsequence between the two strings (each string can have a maximum length
of 50 characters). NOTE: This subsequence need not be contiguous. The input
file may contain empty lines, these need to be ignored.

INPUT SAMPLE:
The first argument will be a path to a filename that contains two strings per
 line, semicolon delimited. You can assume that there is only one unique
 subsequence per test case. E.g.

XMJYAUZ;MZJAWXU

XMJYAUZ
MZJAWXU
['M', 'Z', 'J', 'A', 'X', 'U']

OUTPUT SAMPLE:
The longest common subsequence. Ensure that there are no trailing empty spaces
 on each line you print. E.g.

MJAU
'''

from itertools import imap
from string import rstrip
from sys import argv


def memoize(f):
    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            result = self[key] = f(*key)
            return result

    return memodict().__getitem__


@memoize
def subsequence(string1, string2):

    if string1 and string2:
        char1, rest1 = string1[0], string1[1:]
        char2, rest2 = string2[0], string2[1:]

        if char1 == char2:
            return char1 + subsequence(rest1, rest2)
        else:
            return max(
                subsequence(string1, rest2),
                subsequence(string2, rest1),
                key=len,
            )
    else:
        return ''

with open(argv[1]) as input_file:
    lines = filter(lambda line: line, imap(rstrip, input_file))

for line in lines:
        string1, string2 = line.split(';')

        print subsequence(string1, string2)
