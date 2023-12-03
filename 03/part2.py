file_name = 'input.txt'

matrix = []

for line in open(file_name):
    line = line.strip()
    matrix.append(list(line))

def isGear(x,y):
    if matrix[y][x] != '*':
        return False, None

    adj_nums = adjacent_numbers(x, y)
    if len(adj_nums) == 2:
        return True, adj_nums
    else:
        return False, None

# Given a position that contains a digit,
# return the rest of the number that includes all of the digits
# left/right before a symbol/period
def get_rest_of_number(x, y):
    line = matrix[y]
    number = matrix[y][x]
    
    # Check right
    i = x+1
    while i < len(line):
        value = line[i]
        if value.isdigit():
            number += value
        else:
            break
        i += 1
    
    # Check left
    i = x-1
    while i >= 0:
        value = line[i]
        if value.isdigit():
            number = value + number
        else:
            break
        i -= 1

    return number

# Get the numbers adjacent to the current position
def adjacent_numbers(x, y):
    numbers = []
    
    # Check left
    if x > 0 and matrix[y][x-1].isdigit():
        numbers.append(get_rest_of_number(x-1, y))
    
    # Check right
    if x < len(matrix[y])-1 and matrix[y][x+1].isdigit():
        numbers.append(get_rest_of_number(x+1, y))
    
    # Check row above
    if y > 0:
        line_above = matrix[y-1]
        i = x -1 if x > 0 else x
        last_char = ""
        while i <= x+1:
            value = line_above[i]
            if value.isdigit() and not last_char.isdigit():
                numbers.append(get_rest_of_number(i, y-1))
            last_char = value
            i += 1
    
    # Check row below
    if y < len(matrix)-1:
        line_below = matrix[y+1]
        i = x -1 if x > 0 else x
        last_char = ""
        while i <= x+1:
            value = line_below[i]
            if value.isdigit() and not last_char.isdigit():
                numbers.append(get_rest_of_number(i, y+1))
            last_char = value
            i += 1

    return numbers

gears = []
for l in range(len(matrix)):
    line = matrix[l]
    i = 0

    while i < len(line):
        value = line[i]

        gear, numbers = isGear(i, l)
        if gear:
            gears.append(int(numbers[0]) * int(numbers[1]))
            print("\033[92m" + value + "\033[0m", end="")
        else:
            print(value, end="")

        i += 1
    
    print()

print()
print(gears)
print(sum(gears))