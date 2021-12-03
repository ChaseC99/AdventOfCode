file_name = 'input.txt'

x_pos = 0
depth = 0
aim = 0
for line in open(file_name):
    instruction, val = line.split(' ')
    val = int(val)

    if instruction == 'forward':
        x_pos += val
        depth += aim * val
    elif instruction == 'up':
        aim -= val
    elif instruction == 'down':
        aim += val

print(x_pos, depth, x_pos*depth)
