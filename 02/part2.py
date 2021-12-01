input_file = open("./input.txt")

valid_count = 0
for line in input_file:
    line_vals = line.strip().split()
    i1, i2 = [int(n) for n in line_vals[0].split('-')]
    char = line_vals[1][0]
    pswd = line_vals[2]

    if (pswd[i1-1] == char) ^ (pswd[i2-1] == char):
        valid_count += 1

print(valid_count)
