file_name = 'input.txt'

lines = []
for line in open(file_name):
    lines.append(line.strip())

instructions = lines[0]

class Node:
    def __init__(self, value):
        self.value = value
    
    def add_lr(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value} = ({self.left}, {self.right})"
    
    def __repr__(self):
        return self.__str__()

nodes = dict()

i = 2
while i < len(lines):
    node = lines[i].split(" = ")[0]
    nodes[node] = Node(node)
    i += 1

i = 2
while i < len(lines):
    node, lr = lines[i].split(" = ")
    left, right = lr[1:-1].split(", ")
    nodes[node].add_lr(left, right)

    i += 1

print(nodes)

steps = 0
pos = nodes["AAA"]
while True:
    if pos.value == "ZZZ":
        print(steps)
        break

    instruction = instructions[steps % len(instructions)]
    if instruction == "L":
        pos = nodes[pos.left]
    elif instruction == "R":
        pos = nodes[pos.right]

    steps += 1