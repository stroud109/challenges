"""

1. Find the smallest element in an array of unique numbers

2. Find nth smallest element

3. Find smallest element in a nested list (recursion!)

4. Find lowest int that's /not/ in the random, unique array, e.g. 'find next available server'

Include tests
Determine the run time

"""

import random
import datetime
# import numpy

# Generate array of unique ints


# Option 1:
def generate_unique_array(len_array):
    return random.sample(xrange(1, (len_array * 3)), len_array)

# unique_array = generate_unique_array(10)
# print "unique array: ", unique_array


# Option 2:
# def numpy_generate_unique_array(len_array):
#     return numpy.random.choice(len_array * 3, len_array)

# unique_array = numpy_generate_unique_array(1000)


def find_min(unique_array):
    start = datetime.datetime.utcnow()
    min_num = unique_array[0]

    for i in xrange(len(unique_array)):
        if min_num > unique_array[i]:
            min_num = unique_array[i]

    end = datetime.datetime.utcnow()
    delta = end - start
    print "find_min time: ", delta.total_seconds() * 1000
    print "find_min result: ", min_num
    return min_num

# min_num = find_min(unique_array)
# print "result: ", min_num


def _merge_sort(unique_array):
    if len(unique_array) > 1:
        mid = len(unique_array) / 2
        lefthalf = unique_array[:mid]
        righthalf = unique_array[mid:]

        _merge_sort(lefthalf)
        _merge_sort(righthalf)

        i = 0  # leftshark
        j = 0  # rightshark
        k = 0  # the ultimate source of ordered truth

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                unique_array[k] = lefthalf[i]
                i = i + 1
            else:
                unique_array[k] = righthalf[j]
                j = j + 1
            k = k + 1

        # start with the left half, because we started by moving smaller numbers to the left
        while i < len(lefthalf):
            unique_array[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            unique_array[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return unique_array


def merge_sort_helper(unique_array):
    start = datetime.datetime.utcnow()
    sorted_array = _merge_sort(unique_array)
    end = datetime.datetime.utcnow()
    delta = end - start
    print "merge sort time: ", delta.total_seconds() * 1000
    return sorted_array[0]

# min_num2 = merge_sort_helper(unique_array)
# print "merge sort time: ", min_num2


def find_nth_lowest(nth_lowest, unique_array):
    start = datetime.datetime.utcnow()
    sorted_array = _merge_sort(unique_array)
    end = datetime.datetime.utcnow()
    delta = end - start
    print "nth lowest time: ", delta.total_seconds() * 1000
    try:
        return sorted_array[nth_lowest]
    except:
        return "list is too short"


def find_nested_min(unique_nested_array):

    start = datetime.datetime.utcnow()

    # un-nest the array
    def _reducer(accumulater, curr):
        if isinstance(curr, list):
            reduce(_reducer, curr, accumulater)
        else:
            accumulater.append(curr)
        return accumulater

    formatted_list = reduce(_reducer, unique_nested_array, [])
    end = datetime.datetime.utcnow()
    delta = end - start
    print "find nested min time: ", delta.total_seconds() * 1000

    # then find min
    return find_min(formatted_list)

# min_nested = find_nested_min([29, [26, [17, 9]], [[14, 16], [19, 25, 6, 4]]])
# print "min_nested: ", min_nested


def find_next_available_server(some_array):

    # if the list is empty, all servers are available, so let's use the first one!
    if len(some_array) < 1:
        return 1

    # sort
    sorted_array = sorted(some_array)  # [1, 3, 5]

    for i in xrange(sorted_array[-1]):
        if i + 1 != sorted_array[i]:
            return i + 1

assert find_next_available_server([5, 3, 1]) == 2


def find_next_avail_server(some_array):

    my_set = set(some_array)

    if len(my_set) < 1:
        return 1

    # no need to sort a set

    # let's not iterate to the last int
    # better to use length of set, in this case 3
    # set(1, 2, 100)
    for x in xrange(len(my_set)):
        if x + 1 not in my_set:
            return x + 1

assert find_next_avail_server([100, 2, 1, 1]) == 3
