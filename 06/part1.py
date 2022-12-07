file_name = 'input.txt'

def scan_line(l):
    i = 0
    while True:
        if 4 == len(set(list(l[i:i+4]))):
            return i + 4
        i += 1

for line in open(file_name):
    print(scan_line(line))