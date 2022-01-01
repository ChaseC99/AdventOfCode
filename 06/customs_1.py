file_name = "input.txt"

total_sum = 0
group_ans = set()

# Iterate over file
for line in open(file_name):
    line = line.strip() # Clean up: remove newline char
    
    if not line:
        # End of group
        total_sum += len(group_ans) # Add the total 'yes' ans to sum
        group_ans = set()           # Reset the group
    else:
        for ans in line:
            group_ans.add(ans)      # Add their answer to the set

total_sum += len(group_ans)
print(total_sum)
