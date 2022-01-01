file_name = 'input.txt'

def binary_partition(high, chars, upper_char):
    low = 0
    for c in chars:
        mid = (high - low) // 2 + low
        if c == upper_char:
            low = mid + 1
        else:
            high = mid
    return low

ids = []
for boarding_pass in open(file_name):
    boarding_pass = boarding_pass.strip()
    row = boarding_pass[:7]
    col = boarding_pass[7:]
                
    row_num = binary_partition(127, row, 'B')
    col_num = binary_partition(7, col, 'R')
    seat_id = row_num * 8 + col_num
    ids.append(seat_id)

ids.sort()
prev_id = ids[0]-1
for id in ids:
    if not id - 1 == prev_id:
        print(id-1)
        break
    prev_id = id
