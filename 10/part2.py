# https://adventofcode.com/2023/day/10

file_name = 'demo.txt'

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

pipe = [start, next_position, position]

# Follow the pipe
while True:
	# Move to the next pipe
	position = move(position)
	steps += 1
	if position == None:
		break
	pipe.append(position)

# Remove the last pipe, which is the start again
pipe = pipe[:-1]
print(pipe)

# Create a new map that cleans out all of the non-pipes
new_map = []
for row in range(len(map)):
    new_row = []
    for col in range(len(map[row])):
        if (row, col) in pipe:
            new_row.append(map[row][col])
        else:
            new_row.append('1')
    new_map.append(new_row)

# Start in the top left and iterate through the map recursively, replacing
# each zero with a 1 when it is visited
def visit(row, col):
    if new_map[row][col] == '1':
        new_map[row][col] = '0'
        # Go up
        if row > 0:
            visit(row - 1, col)
			
        # Go down
        if row < len(new_map) - 1:
            visit(row + 1, col)
        
        # Go left
        if col > 0:
            visit(row, col - 1)
			
        # Go right
        if col < len(new_map[row]) - 1:
            visit(row, col + 1)
		
        # Go up-left
        if row > 0 and col > 0:
            visit(row - 1, col - 1)
		
        # Go up-right
        if row > 0 and col < len(new_map[row]) - 1:
            visit(row - 1, col + 1)
			
        # Go down-left
        if row < len(new_map) - 1 and col > 0:
            visit(row + 1, col - 1)
			
        # Go down-right
        if row < len(new_map) - 1 and col < len(new_map[row]) - 1:
            visit(row + 1, col + 1)

# Visit all of the edges
# Top row
for col in range(len(new_map[0])):
    visit(0, col)
# Bottom row
for col in range(len(new_map[0])):
    visit(len(new_map) - 1, col)
# Left column
for row in range(len(new_map)):
    visit(row, 0)
# Right column
for row in range(len(new_map)):
    visit(row, len(new_map[row]) - 1)

print("New map:")
for row in new_map:
	print("".join(row))
