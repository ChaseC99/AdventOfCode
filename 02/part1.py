file_name = 'input.txt'

x_pos = 0
depth = 0
for line in open(file_name):
    instruction, val = line.split(' ')
    val = int(val)

    if instruction == 'forward':
        x_pos += val
    elif instruction == 'up':
        depth -= val
    elif instruction == 'down':
        depth += val

print(x_pos, depth, x_pos*depth)