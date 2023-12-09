# https://adventofcode.com/2023/day/9

file_name = 'input.txt'

extrapolated_sum = 0

for line in open(file_name):
	data = [[int(value) for value in line.strip().split(' ')]]

	while not all(value == 0 for value in data[-1]):
		last_sequence = data[-1]
		new_sequence = []
		for i in range(1, len(last_sequence)):
			new_sequence.append(last_sequence[i] - last_sequence[i-1])
		data.append(new_sequence)
	
	# Iterate backwards through data
	for i in range(len(data)-1, 0, -1):
		data[i - 1].append(data[i][-1] + data[i-1][-1])
		
	extrapolated_sum += data[0][-1]

print(extrapolated_sum)
