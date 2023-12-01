file_name = 'input.txt'

def scan_line(l):
    i = 0
    while True:
        if 14 == len(set(list(l[i:i+14]))):
            return i + 14
        i += 1

for line in open(file_name):
    print(scan_line(line))