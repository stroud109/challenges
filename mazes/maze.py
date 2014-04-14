# -*- coding: latin-1 -*-

from pprint import pprint
import random
import string

EAST = 'E'
NORTH = 'N'
chars = iter(string.ascii_uppercase)

class Tile(object):
    def __init__(self, coords):
        self.name = chars.next()
        self.coords = coords

    def __repr__(self):
        return 'Tile(%s)' % self.name


def generate_edges_and_paths(width, height):

    edges = []
    #generate path instances while getting edges
    tiles_by_coordinates = {}

    for x in range(width):
        for y in range(height):
            tiles_by_coordinates[(x, y)] = set([Tile((x, y))])
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

    return edges, tiles_by_coordinates


def generate_maze(width, height):
    '''
    A function that randomly produces mazes.
    Takes the length and width of a grid as arguments.
    '''

    edges, path_at_tile_coords = generate_edges_and_paths(width, height)

    pprint(edges)
    pprint(path_at_tile_coords)
    print 'original number of edges: ', len(edges)
    print 'original number of path_at_tile_coords: ', len(path_at_tile_coords)

    # If the tile values are the same, add the edge to `walls`.
    # If the tile values are different, merge the values.
    walls = []

    while edges:

        edge = edges.pop(random.randint(0, len(edges) - 1))

        # Calculate coordinates for the tiles that this edge separates.
        a_path_coords = (edge[0], edge[1])

        # If the edge faces east, compare what's above and below the edge.
        if edge[2] == EAST:
            b_path_coords = (edge[0], (edge[1] - 1))

        # If the edge faces north, compare what's on either side of the edge.
        elif edge[2] == NORTH:
            b_path_coords = ((edge[0] - 1), edge[1])

        if not path_at_tile_coords[a_path_coords].intersection(path_at_tile_coords[b_path_coords]):
            joined_path = path_at_tile_coords[a_path_coords].union(path_at_tile_coords[b_path_coords])

            # For each tile in the joined path, we need to go over.
            # 'path_at_tile_coords[tile.coords]' and set the path at that coord to be
            # the joined path:
            for tile in joined_path:
                path_at_tile_coords[tile.coords] = joined_path

        else:
            walls.append(edge)

    pprint(path_at_tile_coords)
    return walls

if __name__ == '__main__':
    print generate_maze(3, 3)

