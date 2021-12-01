file_name = "input.txt"

# Node Class
#   We can represent each adapter as a node in directed graph.
#   The value of the node is the output joltage rating.
#   The children of the nodes are the adapters that it can connect to. 
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    
    def add_child(self, node):
        self.children.append(node)

    def __le__(self, other):
        if type(other) == int: return self.val <= other
        if type(other) == Node: return self.val <= other.val

    def __sub__(self, node):
        return self.val - node.val

    def __repr__(self):
        # Example Format: "1 -> [2, 3]"
        return str(self.val) + " -> " + str([int(node.val) for node in self.children])


# Count Paths
#   A recursive function to determine the number of possible paths from a given Node.
#   Utilizes a cache so that we don't have to compute the number of paths for a node multiple times.
cache = {}  # Cache for memoization
def count_paths(node):
    # Check the cache first
    if node.val in cache:
        return cache[node.val]
    
    # Base case: 
    #   return 1 if you've reached the end of the path
    if node.children == []:
        return 1
    
    # Count the number of paths possible from the children nodes
    paths = 0
    for next_node in node.children:
        paths += count_paths(next_node)
    
    # Save the path count in the cache
    cache[node.val] = paths

    return paths

# MAIN FUNCTION
if __name__ == '__main__':
    # Load all of the adapters from the input file
    adapters = []
    for line in open(file_name):
        node = Node(int(line.strip()))      # Create a Node from the adapter
        adapters.append(node)                  # Add that node to the list

    adapters.sort(key=lambda node: node.val)   # Sort that list by the adapter val


    # Add the children adapter 
    for index in range(len(adapters)):
        adapter = adapters[index]
        for a in range(index+1, index+1+3):
            if a < len(adapters):
                # Get the jolt difference between the 2 adapters
                other_adapter = adapters[a]
                diff = other_adapter - adapter

                # Only a valid child if the difference is <= 3
                if diff <= 3:
                    adapter.add_child(other_adapter)

    # Display the graph
    print("Adapters Graph")
    print(adapters, end='\n\n')    

    # Track the total path count
    total_possible_paths = 0
    
    # We can start from any adapter that has a jolt of 3 or less.
    # So we need to check the first 3 adapaters and 
    # add their possible paths to the total_possible_paths count
    for starting_adapter in adapters[:3]:
        if starting_adapter <= 3:
            total_possible_paths += count_paths(starting_adapter)


    # Print that answer :D
    print("Total possible paths:", total_possible_paths)