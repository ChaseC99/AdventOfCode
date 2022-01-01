file_name = 'input.txt'

instructions = []
for line in open(file_name):
    line = line.strip()
    instruction = line[0]
    value = int(line[1:])
    instructions.append((instruction, value))

N = 'N'
S = 'S'
E = 'E'
W = 'W'
L = 'L'
R = 'R'
F = 'F'

class Ship:
    def __init__(self):
        self.direction = E
        self.x = 0
        self.y = 0
    
    def change_direction(self, direction, rotation):
        turns = rotation // 90
        for i in range(turns):
            if direction == R:
                self._turn_right()
            elif direction == L:
                self._turn_left()

    def _turn_right(self):
        if self.direction == N:
            self.direction = E
        elif self.direction == E:
            self.direction = S
        elif self.direction == S:
            self.direction = W
        elif self.direction == W:
            self.direction = N

    def _turn_left(self):
        if self.direction == N:
            self.direction = W
        elif self.direction == E:
            self.direction = N
        elif self.direction == S:
            self.direction = E
        elif self.direction == W:
            self.direction = S

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f'({self.x}, {self.y}) facing {self.direction}. Manhattan Distance = {self.manhattan_distance()}' 

ship = Ship()

for ins, val in instructions:
    print(ship)
    if ins == N:
        ship.y += val
    elif ins == S:
        ship.y -= val
    elif ins == E:
        ship.x += val
    elif ins == W:
        ship.x -= val
    elif ins == L:
        ship.change_direction(L, val)
    elif ins == R:
        ship.change_direction(R, val)
    elif ins == F:
        ins = ship.direction
        if ins == N:
            ship.y += val
        elif ins == S:
            ship.y -= val
        elif ins == E:
            ship.x += val
        elif ins == W:
            ship.x -= val

print(ship)