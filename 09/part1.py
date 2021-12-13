file_name = 'input.txt'

grid = []

for line in open(file_name):
    row = []
    for num in line.strip():
        row.append(int(num))
    grid.append(row)

adj_pos = [(-1,0), (0,1), (1,0), (0, -1)]

risk_level = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        is_min = True
        val = grid[r][c]
        
        i = 0
        while is_min and i < len(adj_pos): 
            pos = adj_pos[i]
            x = pos[0]+r
            y = pos[1]+c

            if (x >= 0 and x < len(grid) 
            and y >= 0 and y < len(grid[0])
            and grid[x][y] <= val):
                is_min = False
            
            i += 1
        
        if is_min:
            risk_level += val+1
    
print(risk_level)
