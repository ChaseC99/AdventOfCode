file_name = "input2.txt"

visted = set()
instructions = []

for line in open(file_name):
    operation, val = line.strip().split()
    val = int(val)

    instructions.append((operation, val))



def execute_instruction(i, acc, branch, visted):
    if i in visted:
        return 0
    else:
        visted.add(i)

    if i >= len(instructions):
        return acc
    operation, val = instructions[i]

    if operation == 'jmp':
        if branch:
            return max(
                execute_instruction(i+val, acc, True, set(list(visted))),
                execute_instruction(i+1, acc, False, set(list(visted)))
            )
        else:
            return execute_instruction(i+val, acc, branch, set(list(visted)))

    elif operation == 'acc':
        acc += val
        return execute_instruction(i+1, acc, branch, set(list(visted)))

    elif operation == 'nop':
        if branch:
            return max(
                execute_instruction(i+val, acc, False, set(list(visted))),
                execute_instruction(i+1, acc, True, set(list(visted)))
            )
        else:
            return execute_instruction(i+1, acc, branch, set(list(visted)))


print(execute_instruction(0, 0, True, set()))
