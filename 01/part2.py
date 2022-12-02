file_name = 'input.txt'

food=0
sums=[]
for line in open(file_name):
    val = line.strip()
    if val == "":
        sums.append(food)
        food=0
    else:
        food += int(val)

sums.append(food)
sums.sort()

print(sum(sums[-3:]))
