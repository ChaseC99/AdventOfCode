file_name = 'input.txt'
target_number = 2089807806

numbers = []
for line in open(file_name):
    numbers.append(int(line.strip()))

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        acc = sum(numbers[i:j]) 
        if acc == target_number:
            print(numbers[i:j])
            print(numbers[i:j][0])
            print(numbers[i:j][-1])
        
        if acc > target_number:
            break

        
