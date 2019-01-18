def read_coords(s):
	pass

def get_dimensions(s):
	pass

	
def build_empty_grid(height, width):
	pass

def build_grid(s):
	pass

def count_living(grid):
	#Declare a counting var.
	count = 0
	#The first loop to iterate over the first list
	for x in grid:
		#The second loop to iterate within the content of the list
		for y in x:
			#If true is found in y then add one to count
			if y == True:
				count += 1

def any_living(grid):
	pass

def on_grid(grid, r, c):
	pass

def count_neighbors(grid, r, c):
	pass

def next_gen(grid):
	pass

def n_gens(grid, n=20):
	pass

def is_still_life(grid, limit=100):
	pass

def is_cycle(grid, limit=100):
	pass