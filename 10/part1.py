# https://adventofcode.com/2023/day/10

file_name = 'input.txt'

# Load the map
map = []
for line in open(file_name):
	line = line.strip()
	row = []
	for c in line:
		row.append(c)
	map.append(row)

# Find first starting point "S"
start = None
for row in range(len(map)):
	for col in range(len(map[row])):
		if map[row][col] == 'S':
			start = (row, col)

direction = None

def move(position):
	global direction
	row, col = position

	if map[row][col] == '|':
		# Vertical pipe
		if direction == 'up':
			return (row - 1, col)
		elif direction == 'down':
			return (row + 1, col)
		
	elif map[row][col] == '-':
		# Horizontal pipe
		if direction == 'left':
			return (row, col - 1)
		elif direction == 'right':
			return (row, col + 1)
		
	elif map[row][col] == 'L':
		# 90 degree bend, north and east
		if direction == 'down':
			direction = 'right'
			return (row, col + 1)
		elif direction == 'left':
			direction = 'up'
			return (row - 1, col)
	
	elif map[row][col] == 'J':
		# 90 degree bend, north and west
		if direction == 'down':
			direction = 'left'
			return (row, col - 1)
		elif direction == 'right':
			direction = 'up'
			return (row - 1, col)
	
	elif map[row][col] == '7':
		# 90 degree bend, south and west
		if direction == 'up':
			direction = 'left'
			return (row, col - 1)
		elif direction == 'right':
			direction = 'down'
			return (row + 1, col)
	
	elif map[row][col] == 'F':
		# 90 degree bend, south and east
		if direction == 'up':
			direction = 'right'
			return (row, col + 1)
		elif direction == 'left':
			direction = 'down'
			return (row + 1, col)

	# Invalid pipe or back at S
	return None

# Find the a connected pipe
row, col = start
options = []
if row > 0:
	options.append([(row - 1, col), "up"])
if row < len(map) - 1:
	options.append([(row + 1, col), "down"])
if col > 0:
	options.append([(row, col - 1), "left"])
if col < len(map[row]) - 1:
	options.append([(row, col + 1), "right"])

position = start
steps = 0

# Find the first pipe
while True:
	# Move to the next pipe
	next_position, direction = options.pop()
	position = move(next_position)
	if not position == None:
		steps += 1
		break

# Follow the pipe
while True:
	# Move to the next pipe
	position = move(position)
	steps += 1
	if position == None:
		break

print(int(steps/2))