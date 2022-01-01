file_name = 'input.txt'

positions = sorted([int(pos) for pos in open(file_name).readlines()[0].split(',')])
median = positions[int(len(positions)/2)]

fuel = 0
for pos in positions:
    fuel += abs(pos-median)

print(fuel)