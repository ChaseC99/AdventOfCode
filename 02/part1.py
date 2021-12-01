input_file = open("./input.txt")

valid_count = 0
for line in input_file:
    line_vals = line.strip().split()
    min_occ, max_occ = [int(n) for n in line_vals[0].split('-')]
    char = line_vals[1][0]
    pswd = line_vals[2]

    char_count = 0
    for c in pswd:
        if c == char:
            char_count += 1

    if char_count >= min_occ and char_count <= max_occ:
        valid_count += 1

print(valid_count)
