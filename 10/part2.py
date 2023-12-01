file_name = 'input.txt'

x = 1
cycle = 0
crt = ['']

def increment_cycle():
    global x, cycle, crt
    cycle += 1
    crt[-1] = crt[-1] + ('#' if x-1 <= (cycle-1)%40 <= x+1 else '.')

    if cycle % 40 == 0:
        crt.append('')

for line in open(file_name):
    line = line.strip()
    if line.startswith("noop"):
        increment_cycle()
    if line.startswith("addx"):
        val = int(line.split()[1])
        increment_cycle()
        increment_cycle()
        x += val

for row in crt:
    print(row)