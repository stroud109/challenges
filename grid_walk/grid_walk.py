'''
GRID WALK
(https://www.codeeval.com/open_challenges/60/)

CHALLENGE DESCRIPTION:
There is a monkey which can walk around on a planar grid.
The monkey can move one space at a time left, right, up or
down. That is, from (x, y) the monkey can go to (x+1, y),
(x-1, y), (x, y+1), and (x, y-1). Points where the sum of
the digits of the absolute value of the x coordinate plus
the sum of the digits of the absolute value of the y coordinate
are lesser than or equal to 19 are accessible to the monkey.
For example, the point (59, 79) is inaccessible because
5 + 9 + 7 + 9 = 30, which is greater than 19. Another example:
the point (-5, -7) is accessible because abs(-5) + abs(-7) = 5 + 7 = 12,
which is less than 19. How many points can the monkey access if
it starts at (0, 0), including (0, 0) itself?

INPUT SAMPLE:
There is no input for this program.

OUTPUT SAMPLE:
Print the number of points the monkey can access. It should be printed
as an integer - for example, if the number of points is 10, print "10",
not "10.0" or "10.00", etc.
'''


def monkey_can_move(x_coord, y_coord):

    x_nums = map(int, list(str(x_coord)))
    y_nums = map(int, list(str(y_coord)))

    return sum(x_nums) + sum(y_nums) <= 19


def create_grid_position_set(x_coord=0, y_coord=0, grid_set=None):

    if not grid_set:
        grid_set = set()

    if monkey_can_move(x_coord, y_coord):
        grid_set.add((x_coord, y_coord))

        # Because we're only counting absolute values, I'm only going
        # to run the recursion on top, right quadrant and then I'll
        # multiply my results by 4 to get the total spaces.

        if (x_coord, y_coord + 1) not in grid_set:
            create_grid_position_set(x_coord, y_coord + 1, grid_set)

        if (x_coord + 1, y_coord) not in grid_set:
            create_grid_position_set(x_coord + 1, y_coord, grid_set)

    return grid_set


## BONUS:
## To see a pretty grid, uncomment the following lines:
#
# the_grid = create_grid_position_set()
# for i in xrange(300):
#     row = ''
#     for j in xrange(300):
#
#         if (i, j) in the_grid:
#             row += 'x'
#         else:
#             row += '.'
#     print row

print (len(create_grid_position_set()) - 299) * 4 + 1
