file_name = 'input.txt'

class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = []

        if parent == None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

    def add_child(self, child):
        self.children.append(child)

    def get_child(self, c):
        for child in self.children:
            if c == child.name:
                return child
        return None
        
    @property    
    def size(self):
        size = 0
        for child in self.children:
            size += child.size

        return size

    def __str__(self) -> str:
        s = self.name + " (dir, size=" + str(self.size) + ")"
        
        for child in self.children:
            s += "\n" + ("  "*self.depth) + " - " + str(child)
        
        return s

    def __iter__(self):
        for child in self.children:
            yield child

class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self._size = size

    @property
    def size(self):
        return self._size

    def __str__(self) -> str:
        return self.name + " (file, size=" + str(self.size) + ")"


def create_object(input):
    global position
    size, name = input.split(" ")
    if size == 'dir':
        return Dir(name, position)
    else:
        return File(name, int(size))


root = Dir("/", None)
position = root
printing = False

for line in open(file_name):
    line = line.strip()
    if printing:
        if line.startswith("$"):
            printing = False
        else:
            position.add_child(create_object(line))
    
    if line.startswith("$ cd"):
        dir_name = line.split("$ cd ")[1]
        
        if dir_name == "..":
            position = position.parent
        elif dir_name == "/":
            position = root
        else: 
            new_dir = position.get_child(dir_name)
            if new_dir == None:
                new_dir = Dir(dir_name, position)
            position = new_dir

    if line.startswith("$ ls"):
        printing = True

def parse(dir, callback):
    callback(dir)
    for child in dir:
        if type(child) == Dir:
            parse(child, callback)

saved = []
def save_elligible_dir(dir):
    global saved
    if dir.size < 100000:
        saved.append(dir)

print(root)
print("\n\n")

parse(root, save_elligible_dir)
result = 0
for dir in saved:
    result += dir.size
print(result)