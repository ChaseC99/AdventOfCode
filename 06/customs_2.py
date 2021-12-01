file_name = "input.txt"

total_sum = 0
group_ans = set()
new_group = True

for line in open(file_name):
    line = line.strip()
    if not line:
        total_sum += len(group_ans)
        group_ans = set()
        new_group = True
    else:
        if new_group:
            group_ans = set(line)
            new_group = False
        else:
            group_ans &= set(line)

total_sum += len(group_ans)
print(total_sum)
