file_name = 'input.txt'

def letterToValue(letter):
    if letter.isupper():
        return ord(letter)-38
    else:
        return ord(letter)-96

total = 0
for line in open(file_name):
    line = line.strip()
    length = len(line)
    left = set(line[:int(length/2)])
    right = set(line[int(length/2):])

    unique = left.intersection(right)
    
    total += letterToValue(unique.pop())

print(total)