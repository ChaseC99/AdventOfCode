file_name = 'input.txt'

grid = []
for line in open(file_name):
    grid.append([int(h) for h in list(line.strip())])

width = len(grid[0])
height = len(grid)

def compute_score(x, y):
    global grid, width, height

    val = grid[y][x]
    row = grid[y]
    col = [row[x] for row in grid]

    # Left
    left = compute_score_for_direction(x, y, lambda x, y: (x-1, y))
    
    # Right
    right = compute_score_for_direction(x, y, lambda x, y: (x+1, y))
    
    # Up 
    up = compute_score_for_direction(x, y, lambda x, y: (x, y-1))

    # Down
    down = compute_score_for_direction(x, y, lambda x, y: (x, y+1))

    return left * right * up * down

def _is_valid_position(x, y):
    global grid

    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def compute_score_for_direction(x, y, move):
    global grid
    score = 0
    val = grid[y][x]
    
    while True:
        x, y = move(x, y)
        if not _is_valid_position(x, y):
            return score
        score += 1
        if grid[y][x] >= val:
            return score

best_score = 0
for y in range(height):
    for x in range(width):
        best_score = max(compute_score(x, y), best_score)

print(best_score)