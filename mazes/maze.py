# -*- coding: latin-1 -*-

from pprint import pprint
import random
import string

EAST = 'E'
NORTH = 'N'
chars = iter(string.ascii_uppercase)

class Tile(object):
    def __init__(self):
        self.name = chars.next()

    def __repr__(self):
        return 'Tile(%s)' % self.name


def generate_edges_and_paths(width, height):

    edges = []
    #generate path instances while getting edges
    paths = {}

    for x in range(width):
        for y in range(height):
            paths[(x, y)] = set([Tile()])
            if y == 0 and x > 0 and x < width:
                edge = (x, y , NORTH)
                edges.append(edge)
            elif x == 0 and y > 0 and y < height:
                edge = (x, y, EAST)
                edges.append(edge)
            elif y > 0 and y < height and x > 0 and x < width:
                edge_east = (x, y, EAST)
                edge_north = (x, y, NORTH)
                edges.append(edge_east)
                edges.append(edge_north)

    return edges, paths


def generate_maze(width, height):
    '''
    Create a function that randomly produces mazes. This function takes the
    length and width of a grid, signified by `m` and `n`, respectively.
    '''

    edges, paths = generate_edges_and_paths(width, height)

    pprint(edges)
    pprint(paths)
    print 'original number of edges: ', len(edges)
    print 'original number of paths: ', len(paths)

    # if the grid values are the same, add the edge to `walls`
    # if the grid values are different, merge the values
    walls = []

    while edges:

        edge = edges.pop(random.randint(0, len(edges) - 1))
        print '\npopped edge: ', edge
        if edge[2] == EAST:
            # compare what's above and below the edge
            a_path_coords = (edge[0], edge[1])
            b_path_coords = (edge[0], (edge[1] - 1))
            print 'comparing path instances at %s and %s' % (a_path_coords, b_path_coords)
            if not paths[a_path_coords].intersection(paths[b_path_coords]):
                print '>> NOT EQUAL, making them equal'
                joined_path = paths[a_path_coords].union(paths[b_path_coords])
                paths[a_path_coords] = joined_path
                paths[b_path_coords] = joined_path
            else:
                print '>> EQUAL equal, saving edge to list of walls'
                walls.append(edge)

        elif edge[2] == NORTH:
            # compare what's on either side of the edge
            a_path_coords = (edge[0], edge[1])
            b_path_coords = ((edge[0] - 1), edge[1])
            print 'comparing path instances at %s and %s' % (a_path_coords, b_path_coords)
            if not paths[a_path_coords].intersection(paths[b_path_coords]):
                print '>> NOT EQUAL, making them equal'
                joined_path = paths[a_path_coords].union(paths[b_path_coords])
                paths[a_path_coords] = joined_path
                paths[b_path_coords] = joined_path
            else:
                print '>> EQUAL equal, saving edge to list of walls'
                walls.append(edge)

    pprint(paths)
    return walls


if __name__ == '__main__':
    print generate_maze(3, 3)

