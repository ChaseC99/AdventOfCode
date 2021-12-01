file_name = "input1.txt"

visted = set()
instructions = []

for line in open(file_name):
    operation, val = line.strip().split()
    val = int(val)

    instructions.append((operation, val))

acc = 0
i = 0
while i < len(instructions):
    print(i+1)
    if i in visted:
        print('break', acc)
        print(sorted(list(visted)))
        quit()
    
    visted.add(i)

    operation, val = instructions[i]
    if operation == 'jmp':
        i += val
        continue
    elif operation == 'acc':
        acc += val
    
    i += 1

print('end', acc)
    