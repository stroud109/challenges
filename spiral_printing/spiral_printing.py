'''
SPIRAL PRINTING
(https://www.codeeval.com/open_challenges/57/)

CHALLENGE DESCRIPTION:
Write a program to print a 2D array (n x m) in spiral order (clockwise)

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename.
The input file contains several lines. Each line is one test case. Each
line contains three items (semicolon delimited). The first is 'n'(rows),
the second is 'm'(columns) and the third is a single space separated list
of characters/numbers in row major order. E.g.

3;3;1 2 3 4 5 6 7 8 9

1 2 3
4 5 6
7 8 9

OUTPUT SAMPLE:
Print out the matrix in clockwise fashion, one per line, space delimited.
E.g.

1 2 3 6 9 8 7 4 5

'''

from itertools import imap
from string import rstrip
from sys import argv


def spiral_print(tiles):

    spiral = []

    while tiles:

        top_row = tiles.pop(0)
        spiral += top_row

        for row in tiles:
            if row:
                right_side = row.pop()
                spiral.append(right_side)

        if tiles:

            bottom_row = tiles.pop()
            bottom_row.reverse()
            spiral += bottom_row

            rev_indexes = range(len(tiles))
            rev_indexes.reverse()

            for row_index in rev_indexes:
                if tiles[row_index]:
                    left_side = tiles[row_index].pop(0)
                    spiral.append(left_side)

    print ' '.join(map(str, spiral))

with open(argv[1]) as input_file:
    lines = filter(lambda line: line, imap(rstrip, input_file))

for line in lines:
        num_rows, num_cols, coord_string = line.split(';')
        num_cols = int(num_cols)
        num_rows = int(num_rows)
        tile_list = coord_string.split(' ')

        tiles = []

        for i in range(len(tile_list)):
            if i % num_cols == 0:
                row = tile_list[i: i + num_cols]
                if len(tiles) < num_rows:
                    tiles.append(row)

        spiral_print(tiles)
