from collections import defaultdict
file_name = 'demo.txt'

vents_map = defaultdict(int)
count = 0

def update_map(position):
    vents_map[position] += 1
    if vents_map[position] == 2:
        global count
        count += 1

for line in open(file_name):
    pos1, pos2 = line.strip().split(' -> ')
    x1, y1 = [int(val) for val in pos1.split(',')]
    x2, y2 = [int(val) for val in pos2.split(',')]

    min_x, max_x = sorted([x1, x2])
    min_y, max_y = sorted([y1, y2])

    if min_x == max_x:
        for y in range(min_y, max_y+1):
            update_map((min_x, y))
            
    elif min_y == max_y:
        for x in range(min_x, max_x+1):
            update_map((x, min_y))

print(count)
