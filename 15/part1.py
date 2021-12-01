test_input = [0,3,6]
starting_numbers = [5,2,8,16,18,0,1]

nums = starting_numbers

memory = {}

for i in range(len(nums)):
    memory[nums[i]] = i+1

curr = nums[-1]
i = len(nums)

while i <= 30000000:
    if i > 29000000:
        print(curr)
    if curr in memory:
        temp = curr
        curr = i - memory[curr]
        memory[temp] = i
    else:
        memory[curr] = i
        curr = 0

    i += 1

