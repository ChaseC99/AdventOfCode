file_name = "input.txt"

# PART 1: Parse the input file
lines = []
for line in open(file_name):
    lines.append(line.strip())

seeds = [int(seed) for seed in lines[0].split(':')[1].strip().split(' ')]
seed_pairs = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

# Seed pairs are now sorted by their start value
# [(start, length), ...]
print("Seed pairs: ", seed_pairs)

# PART 2: Prepare the maps
i = 2
maps = []
for line in lines:
    if line == '':
        # Ignore empty lines
        pass
    elif line[0].isdigit():
        # Get the destination, source and range length from the line
        destination, source, range_len = [int(value) for value in line.split(' ')]

        # Add the range onto the last map
        maps[-1].append((destination, source, range_len))
    else:
        # Time for a new map
        maps.append([])

for i in range(len(maps)):
    # Sort the maps by their source value
    maps[i] = sorted(maps[i], key=lambda x: x[1])

# Maps are now sorted by their source value
# [[(destination, source, range_len), ...], ...]
print("maps: ", maps)
print()

# PART 3: Processing Seed Ranges
final_ranges = [] # Seed ranges after going through all of the maps: [(start, length), ...]

for seed_pair in seed_pairs:
    # Create a list of seed ranges to process. 
    # Initially, there is only one seed range
    # but as the maps split up the ranges, more will be added to the list
    seed_ranges = [seed_pair]
    for map in maps:
        next_seed_ranges = [] # Ranges have been mapped and will be processed in the next iteration

        # Iterate over the list until it is empty.
        while len(seed_ranges) > 0:
            seed_range = seed_ranges.pop()
            
            # Some ranges will not be mapped, so we need to keep track of that
            mapped = False

            for destination, source, range_len in map:
                # Check if seed_range start is within the map
                if seed_range[0] >= source and seed_range[0] < source + range_len:
                    # Check if seed_range end is within the map
                    if seed_range[0] + seed_range[1] < source + range_len:
                        # Map the entire range
                        next_seed_ranges.append((destination + seed_range[0] - source, seed_range[1]))
                    else:
                        # Map the first part of the range
                        next_seed_ranges.append((destination + seed_range[0] - source, source + range_len - seed_range[0]))
                         
                        # Add the remaining part of the range to the seed_ranges 
                        seed_ranges.append((source + range_len, seed_range[0] + seed_range[1] - source - range_len))
                    
                    mapped = True   # The range has been mapped
                    break           # No need to check the rest of the maps
            
            if not mapped:
                # The range was not mapped, so it remains as is for the next iteration
                next_seed_ranges.append(seed_range)
        
        # Time for the next iteration, so we update the seed_ranges
        seed_ranges = next_seed_ranges

    print("[", seed_pair,"] Final seed ranges: ", sorted(seed_ranges, key=lambda x: x[0]))
    final_ranges.extend(seed_ranges)

print()
print("Final ranges: ", final_ranges)

# PART 4: Find the minimum seed
min_seed = final_ranges[0][0]
for seed_range in final_ranges:
    min_seed = min(min_seed, seed_range[0])

print()
print("Minimum seed: ", min_seed)