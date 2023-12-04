file_name = 'input.txt'

scores = []
for line in open(file_name):
    winners, mine = line.strip().split(":")[1].split("|")
    winners = set(winners.split(" "))
    mine = set(mine.split(" "))

    winners.remove("")
    mine.remove("")

    overlap = len(winners & mine)

    if overlap == 0:
        scores.append(0)
    else:
        scores.append(2 ** (overlap - 1))

print(scores)
print(sum(scores))