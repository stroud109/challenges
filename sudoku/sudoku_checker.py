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

import re
from math import sqrt
from sys import argv

solution_file = open(argv[1])
solution = solution_file.readlines()


def check_array_validity(array):
    d_of_nums = {}
    for i in array:
        if i in d_of_nums:
            return False
        else:
            d_of_nums[i] = True
    return True


def check_board_validity(solution):

    split_solution = solution.split(';')
    board_size = int(split_solution[0])
    board_dimension = int(sqrt(board_size))
    solution_list = split_solution[1]
    solution_list = solution_list.split(',')

    board_solution = []

    for i in range(len(solution_list)):
        if i % board_size == 0:
            row = solution_list[i: i + board_size]
            if len(board_solution) < board_size:
                board_solution.append(row)

    valid = True
    for i in range(board_size):
        column = []
        box1 = []
        box2 = []
        if board_size == 9:
            box3 = []

        for row in board_solution:
            valid = check_array_validity(row)
            if not valid:
                print 'False'
                return False

        for j in range(board_size):
            column.append(board_solution[j][i])

            if i % board_dimension == 0:
                if j < board_dimension:
                    box1 += board_solution[j][i:i + board_dimension]
                elif j < 2 * board_dimension:
                    box2 += board_solution[j][i:i + board_dimension]
                elif board_size == 9:
                    box3 += board_solution[j][i:i + board_dimension]
        column_valid = check_array_validity(column)
        if i % board_dimension == 0:
            box1_valid = check_array_validity(box1)
            box2_valid = check_array_validity(box2)
            if board_size == 9:
                box3_valid = check_array_validity(box3)
        if board_size == 9:
            if not (column_valid and box1_valid and box2_valid and box3_valid):
                print 'False'
                return False
        else:
            if not (column_valid and box1_valid and box2_valid):
                print 'False'
                return False
    print 'True'
    return True

for board in solution:
    board = re.sub(' +', ' ', board)
    board = board.strip()
    if board:
        check_board_validity(board)
