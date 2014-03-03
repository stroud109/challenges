from lev_distance import get_friends_list, organize_network_by_lengths
from unittest import TestCase


class LevDistance(TestCase):

    def test_get_friends_list(self):

        result = get_friends_list(
            'sail',
            {
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

    def test_organize_network_by_lengths(self):

        result = organize_network_by_lengths(['a', 'saailz', 'monkey', 'sails', 'saaps', 'said', 'gail', 'sal', 'sag', 'sa', 'il'])
        expected_result = {
            1: ['a'],
            2: ['sa', 'il'],
            3: ['sal', 'sag'],
            4: ['said', 'gail'],
            5: ['sails', 'saaps'],
            6: ['saailz', 'monkey']
        }
        self.assertEqual(result, expected_result)
