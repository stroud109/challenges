from lowest_unique import find_min
from lowest_unique import merge_sort_helper
from lowest_unique import find_nth_lowest
from lowest_unique import find_nested_min
from unittest import TestCase


UNIQUE_ARRAY = [29, 26, 17, 9, 14, 16, 19, 25, 6, 4]

NESTED_UNIQUE_ARRAY = [29, [26, [17, 9]], [[14, 16], [19, 25, 6, 4]]]


class TestLowestUnique(TestCase):

    def test_lowest_unique(self):
        result = find_min(UNIQUE_ARRAY)
        self.assertEquals(result, 4)

    def test_match_lowest_uniques(self):
        result_iter = find_min(UNIQUE_ARRAY)
        result_merge_sort = merge_sort_helper(UNIQUE_ARRAY)
        self.assertEquals(result_iter, result_merge_sort)

    def test_third_lowest_unique(self):
        result = find_nth_lowest(2, UNIQUE_ARRAY)
        self.assertEquals(result, 9)

    def test_nested_lowest_unique(self):
        result = find_nested_min(NESTED_UNIQUE_ARRAY)
        self.assertEquals(result, 4)
