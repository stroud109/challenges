"""

Return the player position with the lowest unique number.

Example:

Input: 3 3 9 1 6 5 8 1 5 3
Output: 5

"""

from sys import argv


def find_lowest_unique(line):

    num_list = map(lambda x: int(x), line.split(' '))

    sorted_num_list = sorted(num_list)

    min_num = 0

    for i in range(len(num_list) - 1):
        num = sorted_num_list[i]
        num_before = sorted_num_list[i - 1]
        num_after = sorted_num_list[i + 1]

        if i == 0 and num != num_after:
            min_num = num
            break

        elif num != num_before and num != num_after:
            min_num = num
            break

    if min_num == 0:
        print min_num
    else:
        for i in range(len(num_list)):
            if num_list[i] == min_num:
                print i + 1

with open(argv[1]) as input_file:

    for line in input_file:
        find_lowest_unique(line.strip())
