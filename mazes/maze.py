def generate_maze(width, height):

''' Create a function that randomly produces mazes. This function takes the 
length and width of a grid, signified by `m` and `n`, respectively.'''

	edges = []
	EAST = 'E'
	NORTH = 'N'

	# get_edges(width, height)
	for x in range(len(width)):
		for y in range(len(height)):
			if x > 0 and if x < width:
				edge = (x, y, NORTH)
				if edge not in edges: 
					edges.append(edge)
			elif y > 0 and if y < height:
				edge = (x, y, EAST)
				if edge not in edges:
					edges.append(edge)

	# We'll want to keep some edges to make walls on our grid
	keepers = []

	while edges:
		edge = edges.pop(random.randint(0, len(edges) - 1))
		# compare what's on either side of the edge
		# if the grid values are the same, add the edge to `keepers`
		# if the grid values are different, merge the values


		# TBD
