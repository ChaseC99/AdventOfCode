from enum import IntEnum 
file_name = 'input.txt'

class Move(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6
    
def find_move(opp_move, desired_result):
    if desired_result == Result.DRAW:
        return opp_move
    
    move_diff = 1 if desired_result == Result.WIN else -1
    move = opp_move + move_diff
    if move == 0:
        move = 3
    if move == 4:
        move = 1

    return move

score = 0
for line in open(file_name):
    opponent, suggested = line.strip().split(" ")
    opponent = ord(opponent) - 64
    desired_result = (ord(suggested) - 88) * 3

    score += desired_result + find_move(opponent, desired_result)

print(score)