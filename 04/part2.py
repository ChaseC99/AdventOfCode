file_name = 'demo.txt'

cards = []
i = 0
for line in open(file_name):
    winners, mine = line.strip().split(":")[1].split("|")
    winners = set(winners.split(" "))
    mine = set(mine.split(" "))

    winners.remove("")
    mine.remove("")

    cards.append((i, len(winners & mine)))
    i += 1

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

def check_card(card):
    count = 1
    index, num_winners = card

    if num_winners == 0:
        return count

    won_cards = cards[index + 1:index + num_winners + 1]
    for won_card in won_cards:
        count += check_card(won_card)
            
    return count

check_card = memoize(check_card)

count = 0
for card in cards:
    count += check_card(card)

print(count)