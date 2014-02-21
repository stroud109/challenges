'''
Check the validity of a sudoku board
(https://www.codeeval.com/open_challenges/78/)

CHALLENGE DESCRIPTION:

Sudoku is a number-based logic puzzle. It typically comprises of a 9*9 grid
with digits so that each column, each row and each of the nine 3*3 sub-grids
that compose the grid contains all the digits from 1 to 9. For this challenge,
you will be given an N*N grid populated with numbers from 1 through N and you
have to determine if it is a valid sudoku solution. You may assume that N will
be either 4 or 9. The grid can be divided into square regions of equal size,
where the size of a region is equal to the square root of a side of the entire
grid. Thus for a 9*9 grid there would be 9 regions of size 3*3 each.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each
line in this file contains the value of N, a semicolon and the sqaure matrix
of integers in row major form, comma delimited. E.g.

4;1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2
4;2,1,3,2,3,2,1,4,1,4,2,3,2,3,4,1
OUTPUT SAMPLE:

Print out True/False if the grid is a valid sudoku layout. E.g.

True
False
'''

from itertools import imap
from math import sqrt
from string import rstrip
from sys import argv


def is_array_valid(array):

    num_set = set(array)

    if len(num_set) != len(array):
        return False
    else:
        return True


def make_nested_list(solution_list, board_size):

    board_solution = []

    # The board size coorelates to the board length, so we know if `i`
    # is cleanly divisible by the board size we're at the beginning of a row.
    for i in range(len(solution_list)):
        if i % board_size == 0:
            row = solution_list[i: i + board_size]
            if len(board_solution) < board_size:
                board_solution.append(row)

    return board_solution


def check_board_validity(board_size, inner_sq_size, board_solution):

    # We will use the `check_array_validty` function to determine if
    # the value of `row_valid` changes
    row_valid = True

    # Before delving into columns, we can check if all the rows are valid.
    for row in board_solution:
        row_valid = is_array_valid(row)
        if not row_valid:
            return False

    # Now we can iterate through the columns and check the columns and boxes.
    for c in range(board_size):
        column = []
        box1 = []
        box2 = []
        box3 = []

        # We can find all contents for column `i` by iterating over rows.
        for r in range(board_size):
            column.append(board_solution[r][c])

            # Boxes 1, 2 and 3 represent the inner sudoku squares. They are
            # stacked top to bottom, and essentially comprise an extended
            # column. We determine the starting point of the left, middle
            # and right box-columns using the `inner_sq_size` variable.
            if c % inner_sq_size == 0:
                if r < inner_sq_size:
                    box1 += board_solution[r][c:c + inner_sq_size]
                elif r < 2 * inner_sq_size:
                    box2 += board_solution[r][c:c + inner_sq_size]
                elif board_size == 9:
                    box3 += board_solution[r][c:c + inner_sq_size]

        if not is_array_valid(column):
            return False

        if box1 and not is_array_valid(box1):
            return False

        if box2 and not is_array_valid(box2):
            return False

        if box3 and not is_array_valid(box3):
            return False

    return True

with open(argv[1]) as input_file:
    solution = filter(None, imap(rstrip, input_file))

for board in solution:

    # We split the solution into its various components:
    # the board size and the board contents.
    split_board = board.split(';')
    board_size = int(split_board[0])
    inner_sq_size = int(sqrt(board_size))
    solution_string = split_board[1]
    solution_list = solution_string.split(',')

    # `board_solution` will be a list-of-lists, with the inner lists
    # containing the contents of each row.
    board_solution = make_nested_list(solution_list, board_size)

    print check_board_validity(board_size, inner_sq_size, board_solution)
