from minesweeper_oop import Board
from unittest import TestCase

'''
0  1  2  3  4
5  6  7  8  9
10 11 12 13 14
'''

class TestMinesweeperOOP(TestCase):

    def test_get_neighbors_3(self):
        test_board = Board(3, 5, list('**.........*...'))
        neighbors = test_board.get_tile_neighbors(test_board.tiles[3])
        self.assertEqual(len(neighbors), 5)
        self.assertEqual(neighbors[0], test_board.tiles[2])
        self.assertEqual(neighbors[1], test_board.tiles[7])
        self.assertEqual(neighbors[2], test_board.tiles[4])
        self.assertEqual(neighbors[3], test_board.tiles[9])
        self.assertEqual(neighbors[4], test_board.tiles[8])

    def test_get_neighbors_0(self):
        test_board = Board(3, 5, list('**.........*...'))
        neighbors = test_board.get_tile_neighbors(test_board.tiles[0])
        self.assertEqual(len(neighbors), 3)
        self.assertEqual(neighbors[0], test_board.tiles[1])
        self.assertEqual(neighbors[1], test_board.tiles[6])
        self.assertEqual(neighbors[2], test_board.tiles[5])

    def test_get_neighbors_4(self):
        test_board = Board(3, 5, list('**.........*...'))
        neighbors = test_board.get_tile_neighbors(test_board.tiles[4])
        self.assertEqual(len(neighbors), 3)
        self.assertEqual(neighbors[0], test_board.tiles[3])
        self.assertEqual(neighbors[1], test_board.tiles[8])
        self.assertEqual(neighbors[2], test_board.tiles[9])

    def test_get_neighbors_10(self):
        test_board = Board(3, 5, list('**.........*...'))
        neighbors = test_board.get_tile_neighbors(test_board.tiles[10])
        self.assertEqual(len(neighbors), 3)
        self.assertEqual(neighbors[0], test_board.tiles[6])
        self.assertEqual(neighbors[1], test_board.tiles[11])
        self.assertEqual(neighbors[2], test_board.tiles[5])

    def test_get_neighbors_5(self):
        test_board = Board(3, 5, list('**.........*...'))
        neighbors = test_board.get_tile_neighbors(test_board.tiles[5])
        self.assertEqual(len(neighbors), 5)
        self.assertEqual(neighbors[0], test_board.tiles[1])
        self.assertEqual(neighbors[1], test_board.tiles[6])
        self.assertEqual(neighbors[2], test_board.tiles[11])
        self.assertEqual(neighbors[3], test_board.tiles[0])
        self.assertEqual(neighbors[4], test_board.tiles[10])

    def test_get_neighbors_14(self):
        test_board = Board(3, 5, list('**.........*...'))
        neighbors = test_board.get_tile_neighbors(test_board.tiles[14])
        self.assertEqual(len(neighbors), 3)
        self.assertEqual(neighbors[0], test_board.tiles[8])
        self.assertEqual(neighbors[1], test_board.tiles[13])
        self.assertEqual(neighbors[2], test_board.tiles[9])

    def test_complete_board(self):
        test_board = Board(9, 9, list('*....*.*..***.**...*............................*..*.....*...*....*....*.....*...'))
        result = test_board.complete_board()
        expected_result = '*3323*4*13***3**212*4222210111000000001111110002*21*21003*312*2002*3122*00112*111'
        self.assertEqual(result, expected_result)


