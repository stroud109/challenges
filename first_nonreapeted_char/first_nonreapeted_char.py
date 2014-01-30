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

import re
from sys import argv

solution_file = open(argv[1])
solution_list = solution_file.readlines()


def get_first_nonrepeat_char(word):
    char_dict = {}
    for char in word:
        print 'char: ', char
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    # TODO

for word in solution_list:
    word = re.sub(' +', ' ', word)
    word = word.strip()
    if word:
        get_first_nonrepeat_char(word)
