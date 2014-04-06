def generate_maze(width, height):

''' 
Create a function that randomly produces mazes. This function takes the 
length and width of a grid, signified by `m` and `n`, respectively.

0 1 2
3 4 5
6 7 8

tiles = {
	0: (0, 2, EAST), (1, 2, NORTH)
	1: (1, 2, NORTH), (1, 2, EAST), (2, 2, NORTH)
	2: (2, 2, NORTH), (2, 2, EAST)
	3: (0, 1, EAST), (1, 1, NORTH), (0, 2, EAST)
	4: (1, 1, EAST), (2, 1, NORTH), (2, 1, NORTH), (1, 2, EAST)
	5: (2, 1, EAST), (2, 1, NORTH), (2, 2, EAST)
	6: (1, 0, NORTH), (0, 1, EAST)
	7: (1, 0, NORTH), (2, 0, NORTH), (2, 1, EAST)
	8: (2, 0, NORTH), (3, 1, EAST)
}

Tiles() = indexes == immutable set
Paths() = group of tiles that form a maze path
Edges() = walls between indvidual tiles

'''

	EAST = 'E'
	NORTH = 'N'

	class Path(object):
		pass

	# get_paths(width, height)
	paths = {}

	# get_edges(width, height)

	edges = []

	for x in range(width):
		for y in range(height):
			paths[(x, y)] = Path()
			if x > 0 and if x < width:
				edge = (x, y, NORTH)
				if edge not in edges: 
					edges.append(edge)
			elif y > 0 and if y < height:
				edge = (x, y, EAST)
				if edge not in edges:
					edges.append(edge)

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

	# TBD
	return walls

