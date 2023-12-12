# https://adventofcode.com/2023/day/11

file_name = 'demo.txt'

def print_map(map):
	for row in map:
		for col in row:
			print(col, end='')
		print()

# Generate the universe map from the input file
universe_map = []
for line in open(file_name):
	line = line.strip()
	universe_map.append(list(line))

print("Initial universe map:")
print_map(universe_map)
print()

# Expand the universe
# Add an extra row next to any row that is empty
row_gaps = []
r = 0
while r < len(universe_map):
	row = universe_map[r]
	if row.count('.') == len(row):
		row_gaps.append(r)
		universe_map.insert(r, ['+'] * len(row))
		r += 1
	r += 1

# Add an extra column next to any column that is empty
colum_gaps = []
c = 0
while c < len(universe_map[0]):
	col = [row[c] for row in universe_map]
	if col.count('.') + col.count('+') == len(col):
		colum_gaps.append(c)
		for row in universe_map:
			row.insert(c, '+')
		c += 1
	c += 1

print("Row gaps:", row_gaps)
print("Column gaps:", colum_gaps)
print("Expanded universe map:")
print_map(universe_map)
print()

# Get all of the galaxies as coordinates
galaxies = []
for r in range(len(universe_map)):
	for c in range(len(universe_map[0])):
		if universe_map[r][c] == '#':
			galaxies.append((r, c))

# Generate a set of all possible pairs of galaxies
galaxy_pairs = set()
for g1 in galaxies:
	for g2 in galaxies:
		if g1 != g2 and (g2, g1) not in galaxy_pairs:
			galaxy_pairs.add((g1, g2))

print("Number of pairs:", len(galaxy_pairs))

# Find the length of the shortest path between each pair of galaxies
# and add it to the sum
path_sum = 0
for g1, g2 in galaxy_pairs:
    extra_x_diff = 0
    for row_gap in row_gaps:
        g1_r = g1[0]
        g2_r = g2[0]
        if g1_r > row_gap > g2_r or g1_r < row_gap < g2_r:
            extra_x_diff += 9
    
    extra_y_diff = 0
    for column_gap in colum_gaps:
        g1_c = g1[1]
        g2_c = g2[1]
        if g1_c > column_gap > g2_c or g1_c < column_gap < g2_c:
            extra_y_diff += 9

    x_diff = abs(g2[0] - g1[0]) + extra_x_diff
    y_diff = abs(g2[1] - g1[1]) + extra_y_diff
    path_sum += x_diff + y_diff

print("Path sum:", path_sum)