from sys import argv

ROW_RANGE = range(1, 9)
COL_RANGE = range(1, 9)


def find_possible_knight_moves(position):
    # TODO: use regex to check that first char is a letter and second char is a number
    # for now let's just assume that's the case

    # `position` is a string like "a1"
    column, row = list(position)

    c = ord(column) - 96  # change the column from a letter to an int
    n = int(row)  # change the row from a string char to an int

    # knights can perform a 1x2 "L" shape move in any direction on the board (columns a-h, rows 1-8)
    right_double_up = [c + 1, n + 2]
    right_double_down = [c + 1, n - 2]
    left_double_up = [c - 1, n + 2]
    left_double_down = [c - 1, n - 2]
    double_right_up = [c + 2, n + 1]
    double_right_down = [c + 2, n - 1]
    double_left_up = [c - 2, n + 1]
    double_left_down = [c - 2, n - 1]

    moves = [
        right_double_up, right_double_down, left_double_up, left_double_down,
        double_right_up, double_right_down, double_left_up, double_left_down
    ]

    possible_moves = []

    for c, n in moves:
        # only add the move to the list of possible_moves if it falls within the board params
        if c in COL_RANGE and n in ROW_RANGE:
            formatted_move = ''.join([chr(c + 96), str(n)])
            possible_moves.append(formatted_move)

    sorted_list = sorted(possible_moves)
    print ' '.join(sorted_list)

with open(argv[1]) as input_file:

    for line in input_file:
        find_possible_knight_moves(line.strip())
