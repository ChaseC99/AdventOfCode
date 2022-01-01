from copy import deepcopy
file_name = 'input.txt'

file = open(file_name)
lines = file.read().splitlines()

oxygen = deepcopy(lines)
i = 0
while len(oxygen) > 1:
    zeros = []
    ones = []

    for line in oxygen:
        if line[i] == '0':
            zeros.append(line)
        else:
            ones.append(line)
    
    if len(zeros) > len(ones):
        oxygen = zeros
    else:
        oxygen = ones

    i += 1

oxygen = oxygen[0]

coo = deepcopy(lines)
i = 0
while len(coo) > 1:
    zeros = []
    ones = []

    for line in coo:
        if line[i] == '0':
            zeros.append(line)
        else:
            ones.append(line)
    
    if len(zeros) > len(ones):
        coo = ones
    else:
        coo = zeros

    i += 1

coo = coo[0]

print("o2:", oxygen, "  |  co2:", coo)
print(int(oxygen, 2) * int(coo, 2))