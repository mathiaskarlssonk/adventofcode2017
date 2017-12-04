import sys, math, time

# Step 1, lazy calculate distance per added spiral

target = 347991
current_spiral = 1 # Current spiral/circle around center
current_number = 2 # First number we write (after initial 1 in center)
middle_distance = 0 # Distance from current number to starting position
total = 1

while current_number < target:
	amounts_in_this_spiral = total*4+4 # How many coords in this spiral
	current_spiral_numbers = [] # Numbers in this spiral
	middle = current_number+(current_spiral-1) # Number level (x) with starting position
	middle_distance += 2

	for i in range(0, amounts_in_this_spiral):
		current_spiral_numbers.append(current_number)
		current_number += 1

	for number in current_spiral_numbers:
		distance = ((number-middle) % middle_distance) + current_spiral # Distance to middle + distance from middle to starting position
		if number == target:
			print "step1: "+str(distance)

	total += 2
	current_spiral += 1

# Step 2, actually build the spirals in a grid

GRID_SIZE = 15
grid = {}
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
X = 0
Y = 1

for x in range(0, GRID_SIZE): # Create grid (hopefully we can find target before we fill up 15*15)
	grid[x] = {}
	for y in range(0, GRID_SIZE):
		grid[x][y] = 0

def difference(a,b):
	return int(math.fabs(a-b))

def traverse(x, y, direction):
	if direction == UP:
		return [x+1, y]
	if direction == DOWN:
		return [x-1, y]
	if direction == RIGHT:
		return [x, y+1]
	if direction == LEFT:
		return [x, y-1]

def is_adjacent_to(spiral, x, y):
	for coord in spiral:
		spiral_x = coord[0]
		spiral_y = coord[1]
		if difference(spiral_x, x) <= 1:
			if difference(spiral_y, y) <= 1:
				return True
	return False

def calculate(x, y):
	total = 0
	total += grid[x][y+1] # Right
	total += grid[x][y-1] # Left
	total += grid[x+1][y] # Up
	total += grid[x-1][y] # Down
	total += grid[x+1][y+1] # Top right
	total += grid[x+1][y-1] # Top left
	total += grid[x-1][y+1] # Bottom right
	total += grid[x-1][y-1] # Bottom left
	return total

def debug_grid():
	# Make a CSV for debugging visually...
	with open('3.csv', 'w') as f:
		for x in grid:
			out = ""
			for y in grid[x]:
				out += (str(grid[x][y])+",")
			f.write(out[:-1]+"\n")


current_x = GRID_SIZE / 2
current_y = GRID_SIZE / 2

# Starting spiral (just 1 coord in the center of the grid with the value 1)
grid[current_x][current_y] = 1
current_spiral = [[current_x, current_y]]

while True:
	previous_spiral = current_spiral
	current_spiral = []
	while True:
		found = False
		for direction in [UP, LEFT, DOWN, RIGHT]:
			test = traverse(current_x, current_y, direction)
			# Don't "walk" in a direction we've already been in...
			if grid[test[X]][test[Y]] > 0:
				continue
			# Only walk on adjacent coords to the previous spiral
			if is_adjacent_to(previous_spiral, test[X], test[Y]):
				found = True
				current_x = test[X]
				current_y = test[Y]
				current_spiral.append([current_x, current_y])
				num = calculate(current_x, current_y) # Calculates sum of surrounding coords

				if num > target:
					print "step2: "+str(num)
					exit()

				grid[current_x][current_y] = num
				break # Valid path found, start next search by testing up, left, down, right...
		# No direction was valid = this spiral is complete = make the next one
		if not found:
			break