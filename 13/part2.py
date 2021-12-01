from functools import reduce

file_name = "input-part2.txt"

input_file = open(file_name)
bus_times = [None if time == 'x' else int(time) for time in input_file.readline().strip().split(',')]
print(bus_times)

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

dividers = []
remainders = []

index = 0
for time in bus_times:
    if time:
        dividers.append(time)
        remainders.append(time-index)
    index += 1

print(dividers)
print(remainders)
print(chinese_remainder(dividers, remainders))
