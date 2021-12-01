import json
from collections import defaultdict
file_name = "input.txt"

input_json = json.load(open(file_name))

def count_needed_bags(color):
    return sum([child[0]+(child[0]*count_needed_bags(child[1])) for child in input_json[color]])

print(count_needed_bags("shiny gold"))