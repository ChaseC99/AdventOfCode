import math

file_name = 'input.txt'

lines = []
for line in open(file_name):
    values = int(line.strip().split(":")[1].replace(" ", ""))
    lines.append(values)

print(lines)

ways_to_win = []

t = lines[0]
d = lines[1]

# Solve for d = x(t - x)
# d = xt - x^2
# x^2 - xt + d = 0
# x = (t +- sqrt(t^2 - 4d)) / 2
# In python, we need to get the positive and negative roots separately
x_1 = (t - math.sqrt(t**2 - 4*d)) / 2
x_2 = (t + math.sqrt(t**2 - 4*d)) / 2

# Take the ceiling of x_1 and the floor of x_2 (not including the endpoints)
x_1 = math.floor(x_1+1)
x_2 = math.ceil(x_2-1)

# Number of ints between x_1 and x_2, inclusive
ways_to_win = x_2 - x_1 + 1

print(ways_to_win)
