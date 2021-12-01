file_name = 'input.txt'

layout = []

for row_input in open(file_name):
    row = []
    for val in row_input:
        if val == 'L':
            row.append(False)
        elif val == '#':
            row.append(True)
        elif val == '.':
            row.append(None)
    layout.append(row)

neighbors = [
    (-1,-1), (0, -1), (1, -1),
    (-1, 0),          (1, 0),
    (-1, 1), (0, 1),  (1, 1)
]

def _is_valid(x, y):
    return x >= 0 and x < len(layout[0]) and y >= 0 and y < len(layout)

def count_neighbors(layout, x, y):
    count = 0
    for neighbor in neighbors:
        n_x, n_y = neighbor
        neighbor_x = n_x + x
        neighbor_y = n_y + y

        while True:
            if not _is_valid(neighbor_x, neighbor_y) or layout[neighbor_y][neighbor_x] == False:
                break
            if layout[neighbor_y][neighbor_x]:
                count += 1
                break

            neighbor_x += n_x
            neighbor_y += n_y
    
    return count
        

def run_round(layout):
    new_layout = []
    
    for row in range(len(layout)):
        new_row = []
        for col in range(len(layout[row])):
            seat = layout[row][col]
            if seat == None:
                new_row.append(None)
            else:
                neighbors = count_neighbors(layout, col, row)
                
                if neighbors == 0:
                    new_row.append(True)
                elif neighbors >= 5:
                    new_row.append(False)
                else:
                    new_row.append(seat)
        
        new_layout.append(new_row)

    return new_layout


def print_layout(layout):
    for row in layout:
        for val in row:
            if val == None: print('.', end='')
            elif val: print('#', end='')
            else: print('L', end='')
        print()

old_layout = []

while old_layout != layout:
    old_layout = layout
    layout = run_round(layout)


filled_seats = 0
for row in layout:
    for seat in row:
        if seat:
            filled_seats += 1

print_layout(layout)
print("seats", filled_seats)


