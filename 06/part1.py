file_name = 'input.txt'

fishes = [int(fish) for fish in open(file_name).readlines()[0].split(',')]

total_days = 80

for i in range(total_days):
    fish_len = len(fishes)
    for i in range(fish_len):
        if fishes[i] == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1

print("Number of fish: ", len(fishes))