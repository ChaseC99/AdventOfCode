import json
from collections import defaultdict
file_name = "input.txt"

# Regex to reformat input
#   
#   (\d) ([a-z]* [a-z]*) bags?[,\.] -> ($1, "$2"),

input_json = json.load(open(file_name))

inverted_index = defaultdict(set)

for key in input_json:
    nested_bags = input_json[key]
    for bag in nested_bags:
        inverted_index[bag[1]].add(key)

def find_parent(color):
    if not color in inverted_index:
        return set()

    parents = inverted_index[color]
    results = set(list(parents))
    for parent in parents:
        results |= find_parent(parent)
    
    return results

print(len(find_parent("shiny gold")))
