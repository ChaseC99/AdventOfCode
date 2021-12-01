file_name = 'input.txt'

def set_bit(bit, value, index):
    if bit == 0:
        return value & ~(1 << index)
    elif bit == 1:
        return value | (1 << index)

def bit_mask(mask, value):
    i = 0
    for bit in reversed(mask):
        if not bit == 'X':
            value = set_bit(int(bit), value, i)
        i += 1
    
    return value

def main():
    mem = dict()
    mask = None

    for line in open(file_name):
        if line.startswith('mask'):
            mask = line.strip().split(' = ')[1]

        elif line.startswith('mem'):
            line_values = line.strip().split(' = ')
            mem_position = int(line_values[0][4:-1])
            value = int(line_values[1])

            value = bit_mask(mask, value)
            mem[mem_position] = value
    
    print(sum(mem.values()))
            

if __name__ == '__main__':
    main()
