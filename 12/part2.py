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
        self.waypoint = [10, 1]
        self.x = 0
        self.y = 0
    
    def rotate_direction(self, direction, rotation):
        turns = rotation // 90
        for i in range(turns):
            if direction == R:
                self._turn_right()
            elif direction == L:
                self._turn_left()

    def move(self, val):
        self.x += self.waypoint[0] * val
        self.y += self.waypoint[1] * val

    def change_waypoint(self, direction, val):
        if direction == N:
            self.waypoint[1] += val
        elif direction == S:
            self.waypoint[1] -= val
        elif direction == E:
            self.waypoint[0] += val
        elif direction == W:
            self.waypoint[0] -= val


    def _turn_right(self):
        way_x, way_y = self.waypoint
        self.waypoint = [way_y, -way_x]

    def _turn_left(self):
        way_x, way_y = self.waypoint
        self.waypoint = [-way_y, way_x]

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f'Pos: ({self.x}, {self.y}). Way: ({self.waypoint[0]}, {self.waypoint[1]}). Manhattan Distance = {self.manhattan_distance()}' 

ship = Ship()

for ins, val in instructions:
    print(ship)
    if ins == N or ins == S or ins == E or ins == W:
        ship.change_waypoint(ins, val)
    elif ins == L:
        ship.rotate_direction(L, val)
    elif ins == R:
        ship.rotate_direction(R, val)
    elif ins == F:
        ship.move(val)

print(ship)