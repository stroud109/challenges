'''
String Permutations
(https://www.codeeval.com/open_challenges/14/)

CHALLENGE DESCRIPTION:
Write a program to print out all the permutations of
a string in alphabetical order. We consider that
digits < upper case letters < lower case letters.
The sorting should be performed in ascending order.

INPUT SAMPLE:
Your program should accept as its first argument a
path to a file containing an input string, one per line. E.g.

hat
abc
Zu6

OUTPUT SAMPLE:
Print to stdout, permutations of the string, comma separated,
in alphabetical order. E.g.

aht,ath,hat,hta,tah,tha
abc,acb,bac,bca,cab,cba
6Zu,6uZ,Z6u,Zu6,u6Z,uZ6
'''

import re
from itertools import permutations
from sys import argv

solution_file = open(argv[1])
solution_list = solution_file.readlines()


def permutate_string(word):
    # print 'word: ', word
    word_permutations = list(permutations(word))
    # print 'word_permutations: ', word_permutations

    new_word_list = []
    for permutation in word_permutations:
        permutation = ''.join(permutation)
        # print permutation
        new_word_list.append(permutation)
        # print new_word_list

    new_word_list = sorted(new_word_list)
    print ','.join(new_word_list)

for word in solution_list:
    word = re.sub(' +', ' ', word)
    word = word.strip()
    if word:
        permutate_string(word)
