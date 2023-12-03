file_name = 'input.txt'

matrix = []

for line in open(file_name):
    line = line.strip()
    matrix.append(list(line))

# Periods and numbers do not count as a symbol
def isSymbol(value):
    return value != '.'

# Checks to see if there is a symbol adjacent to the current symbol
# Adjacent means left, right, up, down, and diagonally
def adjacent_symbol(line_number, start, end):
    line = matrix[line_number]

    # Check left
    if start > 0 and isSymbol(line[start-1]):
        return True
    
    # Check right
    if end < len(line)-1 and isSymbol(line[end+1]):
        return True

    # Check row above
    if line_number > 0:
        line_above = matrix[line_number-1]
        i = start -1 if start > 0 else start
        while i <= end:
            if isSymbol(line_above[i]):
                return True
            i += 1
        if end < len(line)-1 and isSymbol(line_above[end+1]):
            return True
    
    # Check row below
    if line_number < len(matrix)-1:
        line_below = matrix[line_number+1]
        i = start -1 if start > 0 else start
        while i <= end:
            if isSymbol(line_below[i]):
                return True
            i += 1
        if end < len(line)-1 and isSymbol(line_below[end+1]):
            return True

parts = []
for l in range(len(matrix)):
    line = matrix[l]
    i = 0

    start_i = None
    number = ""

    while i < len(line):
        value = line[i]
        if value.isdigit():
            number += value
            if start_i is None:
                start_i = i

        elif start_i is not None:
            end_i = i-1

            if adjacent_symbol(l, start_i, end_i):
                parts.append(int(number))
                print("\033[92m" + number + "\033[0m", end="")
            else:
                print(number, end="")

            start_i = None
            number = ""
            print(value, end="")
        else:
            print(value, end="")
        i += 1
    
    if start_i is not None:
        end_i = i-1

        if adjacent_symbol(l, start_i, end_i):
            parts.append(int(number))
            print("\033[92m" + number + "\033[0m", end="")
        else:
            print(number, end="")

    print()

print(parts)
print(sum(parts))