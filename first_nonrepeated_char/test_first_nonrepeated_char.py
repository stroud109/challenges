from first_nonrepeated_char import get_first_nonrepeat_char
from unittest import TestCase


class TestFirstNonrepeatedChar(TestCase):

    def test_first_nonrepeat_1(self):
        result = get_first_nonrepeat_char('yellow')
        expected_result = 'y'
        self.assertEquals(result, expected_result)

