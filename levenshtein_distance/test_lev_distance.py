from lev_distance import get_friends_list
from unittest import TestCase


class LevDistance(TestCase):

    def lev_distance_test1(self):
        result = get_friends_list(
            'sail',
            {
                0: [],
                1: ['a'],
                2: ['sa', 'il'],
                3: ['sal', 'sag'],
                4: ['said', 'gail'],
                5: ['sails', 'saaps'],
                6: ['saailz', 'monkey']
            }
        )
        expected_result = 7
        self.assertEqual(result, expected_result)
