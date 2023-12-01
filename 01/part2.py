# Note: ChatGPT assisted with this code
file_name = 'input.txt'

wordToDigit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

values = []
for line in open(file_name):
    line = line.strip()
    firstNumber = ''
    lastNumber = ''

    # Finding the first number
    i = 0
    while i < len(line):
        for word, digit in wordToDigit.items():
            if line[i:].startswith(word):
                firstNumber = digit
                break
            elif line[i].isdigit():
                firstNumber = line[i]
                break
        if firstNumber:
            break
        i += 1

    # Finding the last number
    i = len(line) - 1
    while i >= 0:
        for word, digit in wordToDigit.items():
            if line[:i+1].endswith(word):
                lastNumber = digit
                break
            elif line[i].isdigit():
                lastNumber = line[i]
                break
        if lastNumber:
            break
        i -= 1

    # Compute the value for the line
    if firstNumber and lastNumber:
        value = int(firstNumber + lastNumber)
    elif firstNumber:  # or lastNumber since both are the same if only one is found
        value = int(firstNumber * 2)
    else:
        value = 0  # In case no number is found

    values.append(value)

print(values)
print(sum(values))
    