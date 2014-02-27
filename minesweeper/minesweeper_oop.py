'''
Minesweeper
(https://www.codeeval.com/open_challenges/79/)

CHALLENGE DESCRIPTION:
You will be given an M*N matrix. Each item in this
matrix is either a '*' or a '.'. A '*' indicates a
mine whereas a '.' does not. The objective of the
challenge is to output a M*N matrix where each element
contains a number (except the positions which actually
    contain a mine which will remain as '*') which
indicates the number of mines adjacent to it. Notice
that each position has at most 8 adjacent positions e.g.
left, top left, top, top right, right, ...

INPUT SAMPLE:
Your program should accept as its first argument a path
to a filename. Each line in this file contains M,N, a
semicolon and the M*N matrix in row major form. E.g.

3,5;**.........*...
4,4;*........*......

OUTPUT SAMPLE:
Print out the new M*N matrix (in row major form) with
each position(except the ones with the mines) indicating
how many adjacent mines are there. E.g.

**100
33200
1*100

*100 2210 1*10 1110

0  1  2  3  4
5  6  7  8  9
10 11 12 13 14


'''

from itertools import imap
from string import rstrip
from sys import argv


class Tile(object):

    def __init__(self, position, value):
        self.value = value
        self.position = position
        self.mines_nearby = 0

    def is_mined(self):
        return self.value == '*'

    def __repr__(self):
        return 'Tile(i=%d, v="%s")' % (self.position, self.value)


class Board(object):

    def __init__(self, height, width, tile_values):
        self.height = height
        self.width = width
        self.tiles = [
            Tile(position, value) for position, value in enumerate(tile_values)
        ]

        for tile in self.tiles:
            if tile.is_mined():
                for neighbor in self.get_tile_neighbors(tile):
                    neighbor.mines_nearby += 1

    def get_tile_neighbors(self, tile):

        neighbors = []

        if tile.position % self.width != 0:

            top_left = tile.position - self.width - 1
            if top_left >= 0 and top_left < len(self.tiles):
                neighbors.append(self.tiles[top_left])

            mid_left = tile.position - 1
            if mid_left >= 0 and mid_left < len(self.tiles):
                neighbors.append(self.tiles[mid_left])

            bottom_left = tile.position + self.width - 1
            if bottom_left >= 0 and bottom_left < len(self.tiles):
                neighbors.append(self.tiles[bottom_left])

        if (tile.position + 1) % self.width != 0:

            top_right = tile.position - self.width + 1
            if top_right >= 0 and top_right < len(self.tiles):
                neighbors.append(self.tiles[top_right])

            mid_right = tile.position + 1
            if mid_right >= 0 and mid_right < len(self.tiles):
                neighbors.append(self.tiles[mid_right])

            bottom_right = tile.position + self.width + 1
            if bottom_right >= 0 and bottom_right < len(self.tiles):
                neighbors.append(self.tiles[bottom_right])

        top_center = tile.position - self.width
        if top_center >= 0 and top_center < len(self.tiles):
                neighbors.append(self.tiles[top_center])

        bottom_center = tile.position + self.width
        if bottom_center >= 0 and bottom_center < len(self.tiles):
                neighbors.append(self.tiles[bottom_center])

        return neighbors

    def complete_board(self):
        board_solution = ''

        for tile in self.tiles:
            if tile.is_mined():
                board_solution += '*'
            else:
                board_solution += str(tile.mines_nearby)

        return board_solution


if __name__ == '__main__':

    with open(argv[1]) as input_file:
        solutions = filter(None, imap(rstrip, input_file))

    for solution in solutions:
        split_solution = solution.split(';')
        height, width = split_solution[0].split(',')
        board = Board(int(height), int(width), list(split_solution[1]))
        print board.complete_board()
