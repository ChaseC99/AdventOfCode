file_name = 'input.txt'

# Convert file input to a grid layout
layout = []
for row_input in open(file_name):
    row = []
    for val in row_input:
        if val == 'L':
            row.append(False)
        elif val == '.':
            row.append(None)
    layout.append(row)


# Is Valid
#   Determine if a coordinate is within the grid
#   Returns true if in grid, false if outside
def _is_valid(x, y):
    return x >= 0 and x < len(layout[0]) and y >= 0 and y < len(layout)

# Count Neighbors
#   Returns number of neighboring seats with people in them
neighbors = [
    (-1,-1), (0, -1), (1, -1),
    (-1, 0),          (1, 0),
    (-1, 1), (0, 1),  (1, 1)
]
def count_neighbors(layout, x, y):
    count = 0
    for neighbor in neighbors:
        n_x, n_y = neighbor
        neighbor_x = n_x + x
        neighbor_y = n_y + y

        if _is_valid(neighbor_x, neighbor_y) and layout[neighbor_y][neighbor_x]:
            count += 1
    
    return count
        

# Run Round
#   Given a layout, generate a new seating layout based off the following rules:
#       If seat has 0 neighboors, add a person to that seat
#       If seat has 4+ neighboors, removed the person from that seat
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
                elif neighbors >= 4:
                    new_row.append(False)
                else:
                    new_row.append(seat)
        
        new_layout.append(new_row)

    return new_layout


# Print Layout
#   Prints a layout in the same format as the input
#   Used for debugging purposes
def print_layout(layout):
    for row in layout:
        for val in row:
            if val == None: print('.', end='')
            elif val: print('#', end='')
            else: print('L', end='')
        print()


# MAIN FUNCTION
if __name__ == '__main__':
    old_layout = []

    # Continue to execute `run_round` until the layout does not change
    while old_layout != layout:
        old_layout = layout
        layout = run_round(layout)

    # Count the number of filled seats
    filled_seats = 0
    for row in layout:
        for seat in row:
            if seat:
                filled_seats += 1

    print_layout(layout)
    print("seats", filled_seats)


