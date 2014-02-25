from fizzbuzz import fizzbuzz
from unittest import TestCase


class TestFizzBuzz(TestCase):

    def test_fizzbuzz1(self):
        result = fizzbuzz('2 3 53')
        expected_result = '1 F B F 5 FB 7 F B F 11 FB 13 F B F 17 FB 19 F B F 23 FB 25 F B F 29 FB 31 F B F 35 FB 37 F B F 41 FB 43 F B F 47 FB 49 F B F 53'
        self.assertEquals(result, expected_result)

    # Other possible tests: fizz_is_1, buzz_is_1, fizz_equals_buzz,
    # fizz_greater_than_max



