from minesweeper import complete_minesweeper_board
from unittest import TestCase


class TestMinesweeper(TestCase):

    def test_minesweeper_1(self):
        result = complete_minesweeper_board('9,9', '*....*.*..***.**...*............................*..*.....*...*....*....*.....*...')
        expected_result = '*3323*4*13***3**212*4222210111000000001111110002*21*21003*312*2002*3122*00112*111'
        self.assertEqual(result, expected_result)
