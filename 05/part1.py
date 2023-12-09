file_name = 'input.txt'

class Map:
    def __init__(self, name):
        self.name = name
        self.mappers = []
    
    def add_map(self, map_str):
        destination, source, range_len = [int(value) for value in map_str.split(' ')]
        def mapper(value):
            if value in range(source, source + range_len):
                return destination + (value - source)
            else:
                return value
        self.mappers.append(mapper)

    def map(self, value):
        for mapper in self.mappers:
            mapped_value = mapper(value)
            if mapped_value != value:
                return mapped_value
        
        return value

    def __str__(self) -> str:
        return f'{self.name}'
    
    def __repr__(self) -> str:
        return self.__str__()


lines = []
for line in open(file_name):
    lines.append(line.strip())

seeds = [int(seed) for seed in lines[0].split(':')[1].strip().split(' ')]

i = 2
maps = []
while i < len(lines):
    line = lines[i]

    if line == '':
        pass
    elif line[0].isdigit():
        maps[-1].add_map(line)
    else:
        maps.append(Map(line.split(" ")[0]))
    
    i += 1

min_seed = seeds[0]
for seed in seeds:
    for map in maps:
        seed = map.map(seed)
    min_seed = min(min_seed, seed)

print(min_seed)
