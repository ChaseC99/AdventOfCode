file_name = 'input.txt'

points_map = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

opening_chars = {
    "(", "[", "{", "<"
}

chars_map = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

err_sums = []

for line in open(file_name):
    stack = []
    skip = False

    for char in line.strip():
        if char in opening_chars:
            stack.append(char)
        else:
            opening_char = chars_map[char]
            if stack.pop() != opening_char:
                skip = True
                break
    
    if skip:
        continue

    err_sum = 0
    for char in reversed(stack):
        err_sum *= 5
        err_sum += points_map[char]
    
    if err_sum:
        err_sums.append(err_sum)

err_sums.sort()    
print(err_sums[int(len(err_sums)/2)])