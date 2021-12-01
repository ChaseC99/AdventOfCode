file_name = "input.txt"

jolts = []

for line in open(file_name):
    jolts.append(int(line.strip()))

jolts.sort()

curr = 0

one_diff = 0
three_diff = 0

for j in jolts:
    diff = j - curr
    if diff == 1: one_diff += 1
    elif diff == 3: three_diff += 1
    elif diff > 4: print(diff)
    
    curr = j

three_diff += 1

print("one:", one_diff)
print("three:", three_diff)
