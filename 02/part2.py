file_name = 'input.txt'

sum_power = 0
for line in open(file_name):
    line = line.strip()

    game_id, games = line.split(':')
    game_id = int(game_id.split(' ')[1])

    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    games = games.split(';')
    games = [result.strip().split(', ') for result in games]
    for game in games:
        for outcome in game:
            number, color = outcome.split(' ')
            min_cubes[color] = max(int(number), min_cubes[color])
    
    sum_power += min_cubes['blue'] * min_cubes['green'] * min_cubes['red']
    
print(sum_power)
