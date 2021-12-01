file_name = "input.txt"

input_file = open(file_name)
earliest = int(input_file.readline().strip())
bus_times = [int(time) for time in input_file.readline().strip().split(',')]
print(earliest, bus_times)
curr_time = earliest

while True:
    for time in bus_times:
        if curr_time % time == 0:
            print((curr_time-earliest) * time)
            quit()
    curr_time += 1