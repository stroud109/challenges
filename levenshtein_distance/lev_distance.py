'''
Levenshtein Distance
(https://www.codeeval.com/open_challenges/58/)

CHALLENGE DESCRIPTION:
Two words are friends if they have a Levenshtein distance
of 1 (For details see Levenshtein distance). That is, you
can add, remove, or substitute exactly one letter in word
X to create word Y. A word's social network consists of all
of its friends, plus all of their friends, and all of their
friends' friends, and so on. Write a program to tell us how
big the social network for the given word is, using our word
list.

INPUT SAMPLE:
The first argument will be a path to a filename, containing
words, and the word list to search in. The first N lines of
the file will contain test cases, they will be terminated by
string 'END OF INPUT'. After that there will be a list of words
one per line. E.g

recursiveness
elastic
macrographies
END OF INPUT
aa
aahed
aahs
aalii
...
...
zymoses
zymosimeters

OUTPUT SAMPLE:
For each test case print out how big the social network for the
word is. In sample the social network for the word 'elastic' is
3 and for the word 'recursiveness' is 1. E.g.

1
3
1

Constrains:
Number of test cases N in range(15, 30)
The word list always will be the same and it's length will be
around 10000 words
'''

from sys import argv
import re

input_file = open(argv[1])
input_file_lines = input_file.readlines()


def clean_line(line):
    line = re.sub(' +', ' ', line)
    line = line.strip()
    return line


def get_lev_distance(string1, string2):
    if len(string1) < len(string2):
        return get_lev_distance(string2, string1)

    # len(string1) >= len(string2)
    if len(string2) == 0:
        return len(string1)

    previous_row = xrange(len(string2) + 1)
    for i, char1 in enumerate(string1):
        current_row = [i + 1]
        for j, char2 in enumerate(string2):
            insertions = previous_row[j + 1] + 1
            # j+1 instead of j since previous_row and
            # current_row are one character longer than string2
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (char1 != char2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def get_friends_list(origin_word, all_network, origins_network=None):
    # print 'origin_word: ', origin_word

    if not origins_network:
        origins_network = {}

    for word in all_network:
        # print 'word: ', word
        if word in origins_network:
            continue

        if get_lev_distance(origin_word, word) == 1:
            origins_network[word] = True
            get_friends_list(word, all_network, origins_network)

    return len(origins_network)

test_cases = []
word_network = []
reading_test_cases = True

for line in input_file_lines:
    line = clean_line(line)
    if not line:
        continue
    if 'END OF INPUT' in line:
        reading_test_cases = False
    elif reading_test_cases:
        test_cases.append(line)
    else:
        word_network.append(line)

for word in test_cases:
    clean_line(word)
    if word:
        print get_friends_list(word, word_network)
