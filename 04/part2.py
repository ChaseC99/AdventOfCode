file_name = 'input.txt'

def get_range(r):
    start, end = r.split('-')
    return (int(start), int(end))

total = 0
for line in open(file_name):
    left, right = line.strip().split(",")
    lstart, lend = get_range(left)
    rstart, rend = get_range(right)

    if ((lstart <= rstart) and (lend >= rstart)) or ((rstart <= lstart) and (rend >= lstart)):
        total += 1

print(total)