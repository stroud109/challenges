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

from sys import argv
import re

coordinates_file = open(argv[1])
coordinates = coordinates_file.readlines()


def determine_if_bricks_fit(coordinates_file):

    results = []

    for i, line in enumerate(coordinates):
        line = re.sub(' +', ' ', line)
        line = line.strip()

        if not line:
            continue

        line_results = []
        split_line = line.split('|')
        hole_coordinates = split_line[0].split(' ')
        x_hole_coords = []
        y_hole_coords = []

        for coord in hole_coordinates:

            coord = re.sub(r'[^0-9-]', ' ', coord)
            striped_coord = coord.strip()
            split_coord = striped_coord.split(' ')
            x_hole_coords.append(int(split_coord[0]))
            y_hole_coords.append(int(split_coord[1]))

        # assuming there is a hole, the difference cannot be 0
        hole_width = abs(x_hole_coords[0] - x_hole_coords[1])
        hole_height = abs(y_hole_coords[0] - y_hole_coords[1])
        hole_dimensions = [hole_width, hole_height]
        hole_dimensions.sort()
        bricks = split_line[1].split(';')

        for brick in bricks:
            l_brick_coords = []
            w_brick_coords = []
            d_brick_coords = []
            brick = re.sub(r'[^0-9-]', ' ', brick)
            striped_brick = re.sub(' +', ' ', brick)
            striped_brick = striped_brick.strip()
            split_brick = striped_brick.split(' ')
            brick_id = split_brick[0]
            l_brick_coords.append(int(split_brick[1]))
            l_brick_coords.append(int(split_brick[4]))
            w_brick_coords.append(int(split_brick[2]))
            w_brick_coords.append(int(split_brick[5]))
            d_brick_coords.append(int(split_brick[3]))
            d_brick_coords.append(int(split_brick[6]))

            brick_length = abs(l_brick_coords[0] - l_brick_coords[1])
            brick_width = abs(w_brick_coords[0] - w_brick_coords[1])
            brick_depth = abs(d_brick_coords[0] - d_brick_coords[1])
            brick_dimensions = [brick_length, brick_width, brick_depth]
            brick_dimensions.sort()

            if brick_dimensions[0] <= hole_dimensions[0]:
                if brick_dimensions[1] <= hole_dimensions[1]:
                    line_results.append(brick_id)

        if not line_results:
            line_results.append('-')

        results.append(line_results)

    for result in results:
        print ','.join(result)

determine_if_bricks_fit(coordinates_file)
