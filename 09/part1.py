file_name = 'input.txt'

numbers = []
for line in open(file_name):
    numbers.append(int(line.strip()))


def valid_number(index):
    num = numbers[index]
    two_sum = set()
    
    for val in numbers[index-25:index]:
        if val in two_sum:
            return True
        else:
            two_sum.add(num-val)

    return False

i = 25
while i < len(numbers):
    if not valid_number(i):
        print(i, ":", numbers[i])
        quit()
    i += 1
