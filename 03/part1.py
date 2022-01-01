from collections import defaultdict
file_name = 'input.txt'

file = open(file_name)
lines = file.readlines()

bit_count = []
for bit in lines[0].strip():
    count = defaultdict(int)
    count[bit] += 1
    bit_count.append(count)
    
for line in lines[1:]:
    line = line.strip()
    for index in range(len(line)):
        bit = line[index]
        bit_count[index][bit] += 1 

gamma = ''
epsilon = ''
for bit in bit_count:
    if bit['0'] > bit['1']:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print('gamma', gamma)
print('epsilon', epsilon)

print(gamma * epsilon)