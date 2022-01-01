file_name = 'input.txt'

fish_days = [0]*9

fishes = [int(fish) for fish in open(file_name).readlines()[0].split(',')]
for fish in fishes:
    fish_days[fish] += 1
fish_days.reverse()

total_days = 256

for i in range(total_days):
    prev = 0
    for day in range(9):
        prev, fish_days[day] = fish_days[day], prev

    fish_days[0] += prev
    fish_days[2] += prev

print("Number of fish: ", sum(fish_days))