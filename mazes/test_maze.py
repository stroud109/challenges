from maze import generate_edges_and_paths
from unittest import TestCase


class TestGenerateEdgesAndPaths(TestCase):

    def test_generates_correct_num_edges(self):
        edges, paths = generate_edges_and_paths(3,3)
        self.assertEqual(len(edges), 12)

    def test_generates_correct_num_paths(self):
        edges, paths = generate_edges_and_paths(3,3)
        self.assertEqual(len(paths), 9)
