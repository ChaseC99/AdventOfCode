file_name = 'input.txt'

def letterToValue(letter):
    if letter.isupper():
        return ord(letter)-38
    else:
        return ord(letter)-96

total = 0
group = []
def checkGroup():
    global group
    global total
    if len(group) == 3:
        unique = group[0].intersection(group[1]).intersection(group[2])
        print(unique)
        total += letterToValue(unique.pop())
        group = []

for line in open(file_name):
    checkGroup()
    group.append(set(line.strip()))

checkGroup()    
print(total)