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
    
def result(your_move, opp_move):
    if your_move == opp_move:
        return Result.DRAW
    
    if (your_move == Move.ROCK and opp_move == Move.PAPER) or (your_move == Move.PAPER and opp_move == Move.SCISSORS) or (your_move == Move.SCISSORS and opp_move == Move.ROCK):
            return Result.LOSS
    
    return Result.WIN

score = 0
for line in open(file_name):
    opponent, suggested = line.strip().split(" ")
    opponent = ord(opponent) - 64
    suggested = ord(suggested) - 87

    score += suggested + result(suggested, opponent)

print(score)