file_name = 'input.txt'

sum=0
maxSum=0
for line in open(file_name):
    val = line.strip()
    maxSum = max(sum, maxSum)
    sum = 0 if val == "" else sum + int(val)

maxSum = max(sum, maxSum)

print(maxSum)
