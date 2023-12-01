file_name = 'input.txt'

values = []
for line in open(file_name):
    # remove nondigit characters
    line = ''.join([i for i in line if i.isdigit()])
    value = line[0] + line[-1]
    value = int(value)
    values.append(value)

print(values)
print(sum(values))
    