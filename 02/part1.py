file_name = 'input.txt'

limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

valid_games = []

# game is ["number color", "number color", ...]
def valid_game(game):
    for outcome in game:
        number, color = outcome.split(' ')
        if int(number) > limits[color]:
            return False
    return True

for line in open(file_name):
    line = line.strip()

    game_id, games = line.split(':')
    game_id = int(game_id.split(' ')[1])

    games = games.split(';')
    games = [result.strip().split(', ') for result in games]
    if all([valid_game(game) for game in games]):
        valid_games.append(game_id)

print(valid_games)
print(sum(valid_games))
