from maze import generate_edges_and_paths, EAST, NORTH
from unittest import TestCase


class TestGenerateEdgesAndPaths(TestCase):

    def test_generates_correct_num_edges(self):
        edges, paths = generate_edges_and_paths(3,3)
        self.assertEqual(len(edges), 12)

    def test_generates_correct_num_paths(self):
        edges, paths = generate_edges_and_paths(3,3)
        self.assertEqual(len(paths), 9)

    def test_generates_correct_num_east_edges(self):
        edges, paths = generate_edges_and_paths(3,3)
        east_edges = filter(lambda e: e[2] == EAST, edges)
        self.assertEqual(len(east_edges), 6)

    def test_generates_correct_num_north_edges(self):
        edges, paths = generate_edges_and_paths(3,3)
        north_edges = filter(lambda e: e[2] == NORTH, edges)
        self.assertEqual(len(north_edges), 6)
