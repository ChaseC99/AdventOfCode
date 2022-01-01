file_name = 'input.txt'

depth_increases = -3
sliding_window = [0, 0, 0]
prev_window_sum = 0
for line in open(file_name):
    depth = int(line.strip())
    sliding_window = sliding_window[1:] + [depth]
    window_sum = sum(sliding_window)
    if window_sum > prev_window_sum:
        depth_increases += 1
    prev_window_sum = window_sum

print(depth_increases)