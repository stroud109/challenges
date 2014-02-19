'''
A Pile of Bricks
https://www.codeeval.com/open_challenges/117/

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.
The input file contains several lines. Each line is one test case.

Each line contains coordinates of opposite vertices of a hole (before the
 vertical bar) separated by space bar and the list of bricks you need to
check. Each brick is enclosed in parentheses where the 1st number is a
brick's index number, the 2nd and 3rd group of numbers are brick's coordinates
of opposite vertices (separated by a space bar), each brick is divided by
semicolon. E.g.

[4,3] [3,-3]|(1 [10,9,4] [9,4,2])
[-1,-5] [5,-2]|(1 [4,7,8] [2,9,0]);(2 [0,7,1] [5,9,8])
[-4,-5] [-5,-3]|(1 [4,8,6] [0,9,2]);(2 [8,-1,3] [0,5,4])

OUTPUT SAMPLE:

For each set of bricks produce a list of bricks (their index numbers
separated by comma) that can pass through the hole. E.g.

1
1,2
-

Constraints:
Coordinates are in range [-100, 100]
There might be up to 15 bricks you need to check.
'''

from itertools import imap
from string import rstrip
from sys import argv
import re


def determine_if_bricks_fit(line):

    results = []
    line_results = []

    # First, we seperate brick coords from hole coords.
    split_line = line.split('|')

    # Next, we reformat all hole coords.
    hole_coordinates = split_line[0]
    coords = re.sub(r'[^0-9-]', ' ', hole_coordinates)
    striped_coord = re.sub(' +', ' ', coords)
    striped_coord = striped_coord.strip()
    split_coord = striped_coord.split(' ')

    # After reformatting, we split the hole's dimensions.
    hole_width = abs(int(split_coord[0]) - int(split_coord[2]))
    hole_height = abs(int(split_coord[1]) - int(split_coord[3]))
    hole_dimensions = [hole_width, hole_height]
    hole_dimensions.sort()

    # Next, we seperate and reformat the different bricks.
    bricks = split_line[1].split(';')

    for brick in bricks:

        brick = re.sub(r'[^0-9-]', ' ', brick)
        striped_brick = re.sub(' +', ' ', brick)
        striped_brick = striped_brick.strip()

        # After reformatting, we split a brick's coordinates.
        split_brick = striped_brick.split(' ')
        brick_id = split_brick[0]
        brick_length = abs(int(split_brick[1]) - int(split_brick[4]))
        brick_width = abs(int(split_brick[2]) - int(split_brick[5]))
        brick_depth = abs(int(split_brick[3]) - int(split_brick[6]))
        brick_dimensions = [brick_length, brick_width, brick_depth]
        brick_dimensions.sort()

        # Now we check if bricks fit through the hole.
        if brick_dimensions[0] <= hole_dimensions[0]:
            if brick_dimensions[1] <= hole_dimensions[1]:
                line_results.append(brick_id)

    if not line_results:
        line_results.append('-')

    results.append(line_results)

    for result in results:
        result = sorted(result, key=lambda x: x if x == '-' else int(x))
        return ','.join(result)

with open(argv[1]) as input_file:
    lines = filter(lambda line: line, imap(rstrip, input_file))

for line in lines:
    print determine_if_bricks_fit(line)
