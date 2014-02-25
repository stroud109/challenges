'''
First Non-repeated Character
(https://www.codeeval.com/open_challenges/12/)

CHALLENGE DESCRIPTION:
Write a program to find the first non repeated character in a string.

INPUT SAMPLE:
The first argument will be a path to a filename containing strings. E.g.

yellow
tooth

OUTPUT SAMPLE:
Print to stdout, the first non repeating character, one per line. E.g.
y
h
'''

from collections import OrderedDict
from itertools import imap
from string import rstrip
from sys import argv


def get_first_nonrepeat_char(word):
    char_dict = OrderedDict()
    for char in word:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    for key, value in char_dict.iteritems():
        if value == 1:
            return key
            break

if __name__ == '__main__':

    with open(argv[1]) as input_file:
        solution_list = filter(None, imap(rstrip, input_file))

    for word in solution_list:
        print get_first_nonrepeat_char(word)
