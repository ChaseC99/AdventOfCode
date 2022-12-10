file_name = 'input.txt'

visited = set()
h_pos = (0, 0)
t_pos = (0, 0)

visited.add(t_pos)

def invert_direction(direction):
    if (direction == 'U'):
        return 'D'
    if (direction == 'D'):
        return 'U'
    if (direction == 'R'):
        return 'L'
    if (direction == 'L'):
        return 'R'

def move(pos, direction):
    if (direction == 'U'):
        return (pos[0], pos[1]+1)
    if (direction == 'D'):
        return (pos[0], pos[1]-1)
    if (direction == 'R'):
        return (pos[0]+1, pos[1])
    if (direction == 'L'):
        return (pos[0]-1, pos[1])

def are_touching(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    return abs(x2-x1) <= 1 and abs(y2-y1) <= 1
        

for line in open(file_name):
    direction, times = line.strip().split()
    for i in range(int(times)):
        h_pos = move(h_pos, direction)
        
        if not are_touching(h_pos, t_pos):
            t_pos = h_pos
            t_pos = move(t_pos, invert_direction(direction))
            visited.add(t_pos)

print(len(visited))