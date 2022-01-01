file_name = 'input.txt'

depth_increases = -1
prev_depth = 0
for line in open(file_name):
    depth = int(line.strip())
    if depth > prev_depth:
        depth_increases += 1
    prev_depth = depth

print(depth_increases)