file_name = 'demo.txt'

def invert_direction(direction):
    if (direction == 'U'):
        return 'D'
    if (direction == 'D'):
        return 'U'
    if (direction == 'R'):
        return 'L'
    if (direction == 'L'):
        return 'R'

class Rope:
    def __init__(self, name, leads=None) -> None:
        self.name = name
        # self.position = (11,15)
        self.position = (0,20)
        self.visited = set()
        self.leads = leads

        self.visited.add(self.position)

    def move_to(self, position):
        original_pos = self.position
        self.position = position

        self.visited.add(self.position)

        if self.leads and not self.touches(self.leads):
            if abs(self.x-self.leads.x) <= 1 ^ abs(self.y-self.leads.y) <= 1:
                self.leads.move_to(original_pos)
            else:
                self.leads.move(None, (self.x-original_pos[0], self.y-original_pos[1]))


    def move(self, direction, offset=None):
        original_pos = self.position

        if offset:
            self.position = (self.x+offset[0], self.y+offset[1])
        if (direction == 'U'):
            self.position = (self.x, self.y-1)
        if (direction == 'D'):
            self.position = (self.x, self.y+1)
        if (direction == 'R'):
            self.position = (self.x+1, self.y)
        if (direction == 'L'):
            self.position = (self.x-1, self.y)

        self.visited.add(self.position)

        if self.leads and not self.touches(self.leads):
            if abs(self.x-self.leads.x) == abs(self.y-self.leads.y):
                self.leads.move(None, (self.x-original_pos[0], self.y-original_pos[1]))
            else:
                self.leads.move_to(original_pos)

    def touches(self, rope):
        return abs(self.x-rope.x) <= 1 and abs(self.y-rope.y) <= 1

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    def __str__(self) -> str:
        return f"{self.name}: ({str(self.x)}, {str(self.y)})"

    def __repr__(self) -> str:
        return self.__str__()

r9 = Rope("r9", )
r8 = Rope("r8", r9)
r7 = Rope("r7", r8)
r6 = Rope("r6", r7)
r5 = Rope("r5", r6)
r4 = Rope("r4", r5)
r3 = Rope("r3", r4)
r2 = Rope("r2", r3)
r1 = Rope("r1", r2)
head = Rope("head", r1)

ropes = [r9, r8, r7, r6, r5, r4, r3, r2, r1, head]

def invert_direction(direction):
    if (direction == 'U'):
        return 'D'
    if (direction == 'D'):
        return 'U'
    if (direction == 'R'):
        return 'L'
    if (direction == 'L'):
        return 'R'

def print_grid():
    grid = []
    for i in range(21):
        grid.append(['.']*26)
    
    for rope in ropes:
        grid[rope.y][rope.x] = rope.name[-1]

    for r in range(21):
        for val in grid[r]:
            print(val, end='')
        print()


for i in range(4):
    head.move("R") 
    
for i in range(4):
    print_grid()
    print(ropes)
    print("=========")
    head.move("U")

# for line in open(file_name):
#     print_grid()
#     print("================ " + line.strip() + " ================")
#     direction, times = line.strip().split()
#     for i in range(int(times)):
#         head.move(direction) 

print(len(r9.visited))