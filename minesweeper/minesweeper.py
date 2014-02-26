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

'''

from itertools import imap
from string import rstrip
from sys import argv


def position_is_validity(i, board):
    if i >= 0 and i < len(board):
        return True


def left_edge_position(i, board_width):
    if i % board_width == 0:
        return True


def right_edge_position(i, board_width):
    return left_edge_position(i + 1, board_width)


def position_not_mined(i, board):
    if position_is_validity(i, board):
        if board[i] != '*':
            return True


def complete_minesweeper_board(dimensions, board):
    board_dimensions = dimensions.split(',')
    board_height = int(board_dimensions[0])
    board_width = int(board_dimensions[1])
    board = list(board)

    for i in range(len(board)):
        if board[i] == '.':
            board[i] = 0

    top_left = -board_width - 1
    top_center = -board_width
    top_right = -board_width + 1
    mid_left = -1
    mid_right = 1
    bottom_left = board_width - 1
    bottom_center = board_width
    bottom_right = board_width + 1

    for i, elem in enumerate(board):

        if elem == '*':
            if not left_edge_position(i, board_width):
                if position_not_mined(i + top_left, board):
                    board[i + top_left] += 1
                if position_not_mined(i + mid_left, board):
                    board[i + mid_left] += 1
                if position_not_mined(i + bottom_left, board):
                    board[i + bottom_left] += 1
            if not right_edge_position(i, board_width):
                if position_not_mined(i + top_right, board):
                    board[i + top_right] += 1
                if position_not_mined(i + mid_right, board):
                    board[i + mid_right] += 1
                if position_not_mined(i + bottom_right, board):
                    board[i + bottom_right] += 1
            if position_not_mined(i + top_center, board):
                board[i + top_center] += 1
            if position_not_mined(i + bottom_center, board):
                board[i + bottom_center] += 1

    assert len(board) == board_height * board_width

    return ''.join(str(tile) for tile in board)

if __name__ == '__main__':

    with open(argv[1]) as input_file:
        solutions = filter(None, imap(rstrip, input_file))

    for solution in solutions:
        split_solution = solution.split(';')
        dimensions = split_solution[0]
        board = split_solution[1]
        print complete_minesweeper_board(dimensions, board)
