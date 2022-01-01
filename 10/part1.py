file_name = 'input.txt'

points_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
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

syntax_err_sum = 0

for line in open(file_name):
    stack = []

    for char in line.strip():
        if char in opening_chars:
            stack.append(char)
        else:
            opening_char = chars_map[char]
            if stack.pop() != opening_char:
                syntax_err_sum += points_map[char]
                break

print(syntax_err_sum)