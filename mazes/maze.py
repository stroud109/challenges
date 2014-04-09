# -*- coding: latin-1 -*-

import random

EAST = 'E'
NORTH = 'N'

class Path(object):
    pass


def generate_edges_and_paths(width, height):

    edges = []
    #generate path instances while getting edges
    paths = {}

    for x in range(width):
        for y in range(height):
            paths[(x, y)] = Path()
            if x > 0 and x < width:
                edge = (x, y, NORTH)
                if edge not in edges:
                    edges.append(edge)
            elif y > 0 and y < height:
                edge = (x, y, EAST)
                if edge not in edges:
                    edges.append(edge)

    return edges, paths


def generate_maze(width, height):
    '''
    Create a function that randomly produces mazes. This function takes the
    length and width of a grid, signified by `m` and `n`, respectively.

    Tiles() = indexes == immutable set
    Paths() = group of tiles that form a maze path
    Edges() = walls between indvidual tiles
    '''

    edges, paths = generate_edges_and_paths(width, height)

    # if the grid values are the same, add the edge to `walls`
    # if the grid values are different, merge the values
    walls = []

    while edges:

        edge = edges.pop(random.randint(0, len(edges) - 1))

        if edge[2] == EAST:
            # compare what's above and below the edge
            a_path_coords = (edge[0], edge[1])
            # if the edges were correctly recorded, all values here should be valid
            b_path_coords = (edge[0], (edge[1] + width))
            if paths[a_path_coords] is not paths[b_path_coords]:
                paths[a_path_coords] = paths[b_path_coords]
            else:
                walls.append(edge)


        elif edge[2] == NORTH:
            # compare what's on either side of the edge
            a_path_coords = (edge[0], edge[1])
            # if the edges were correctly recorded, all values here should be valid
            b_path_coords = ((edge[0] + 1), edge[1])
            if paths[a_path_coords] is not b_path_coords:
                paths[a_path_coords] = paths[b_path_coords]
            else:
                walls.append(edge)

    return walls


if __name__ == '__main__':
    print generate_maze(width, height)

