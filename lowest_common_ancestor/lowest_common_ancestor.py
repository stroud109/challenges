'''
Lowest Common ancestor
(https://www.codeeval.com/open_challenges/11/)

CHALLENGE DESCRIPTION:
Write a program to determine the lowest common ancestor
of two nodes in a binary search tree. You may hardcode
the following binary search tree in your program:

    30
    |
  ____
  |   |
  8   52
  |
____
|   |
3  20
    |
   ____
  |   |
  10 29

INPUT SAMPLE:
The first argument will be a path to a filename containing
2 values that represent two nodes within the tree, one per
line. E.g.

8 52
3 29

OUTPUT SAMPLE:
Print to stdout, the least common ancestor, one per line. E.g.

30
8

'''

from sys import argv
import re

num_file = open(argv[1])
nums = num_file.readlines()

# NUM_TREE = {
#     30: {
#         8: {
#             3: None,
#             20: {
#                 10: None,
#                 29: None
#             }
#         },
#         52: None
#     }
# }

ANCESTORS = {
    10: [10, 20, 8, 30],
    29: [29, 20, 8, 30],
    3: [3, 8, 30],
    20: [20, 8, 30],
    8: [8, 30],
    52: [52, 30],
    30: [30]
}


def get_lowest_common_ancestor(node1, node2):
    node1 = int(node1)
    node2 = int(node2)

    if node1 in ANCESTORS and node2 in ANCESTORS:
        for i in ANCESTORS[node1]:
            for j in ANCESTORS[node2]:
                if i == j:
                    return i

for num_pair in nums:
    num_pair = re.sub(' +', ' ', num_pair)
    num_pair = num_pair.strip()
    if num_pair:
        print get_lowest_common_ancestor(*num_pair.split(' '))
