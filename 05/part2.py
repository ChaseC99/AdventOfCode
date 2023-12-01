file_name = 'input.txt'
map_end = 8

def parse_line(l):
    parsed = []
    length = len(l)
    i = 1
    while i < length:
        if l[i].isalpha():
            parsed.append(l[i])
        else:
            parsed.append(None)
        
        i += 4
    
    return parsed

lines = []
for line in open(file_name):
    lines.append(line.strip('\n'))

parsed_lines = []
for i in range(map_end):
    parsed_lines.append(parse_line(lines[i]))

cols = []
for i in range(len(parsed_lines[0])):
    cols.append([])

for line in parsed_lines:
    for i in range(len(line)):
        if line[i]:
            cols[i].insert(0, line[i])

def read_instr(l):
    _, amount, __, f, ___, t = l.split(' ')
    
    return (int(amount), int(f)-1, int(t)-1)

def act(amount, f, t):
    global cols
    vals = cols[f][(-1 * amount):]
    cols[f] = cols[f][:(-1 * amount)]
    cols[t] += vals
        

for i in range(map_end+2, len(lines)):
    amount, f, t = read_instr(lines[i])
    act(amount, f, t)

for col in cols:
    print(col[-1], end='')

print()