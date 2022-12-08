file_name = 'input.txt'

grid = []
for line in open(file_name):
    grid.append([int(h) for h in list(line.strip())])

width = len(grid[0])
height = len(grid)

def is_visible(x, y):
    global grid, width, height

    val = grid[y][x]
    row = grid[y]
    col = [row[x] for row in grid]

    return (x == 0 or x+1 == width      # Check left/right border
        ) or (y == 0 or y+1 == height   # Check up/down border
        ) or (max(row[:x]) < val        # Check left
        ) or (max(row[x+1:]) < val      # Check right
        ) or (max(col[:y]) < val        # Check up
        ) or (max(col[y+1:]) < val      # Check down
        )

count = 0
for y in range(height):
    for x in range(width):
        if is_visible(x, y):
            count += 1
print(count)
