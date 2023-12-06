import math

file_name = 'input.txt'

lines = []
for line in open(file_name):
    values = [int(value) for value in line.strip().split(":")[1].split(" ") if value != ""]
    lines.append(values)

ways_to_win = []

times = lines[0]
distances = lines[1]
for i in range(len(times)):
    t = times[i]
    d = distances[i]

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
    num_ints = x_2 - x_1 + 1

    ways_to_win.append(num_ints)

print(ways_to_win)

# Multiply all the ways to win together
ways_to_win_product = 1
for ways in ways_to_win:
    ways_to_win_product *= ways

print(ways_to_win_product)