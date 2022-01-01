file_name = 'input.txt'

def set_bit(bit, value, index):
    if bit == '1':
        return [value | (1 << index)]
    elif bit == 'X':
        return [value & ~(1 << index), value | (1 << index)]
    else:
        return [value]
    

def generate_addresses(mask, value):
    index = 0

    addresses = [value]

    for bit in reversed(mask):
        new_addresses = []
        for address in addresses:
            new_addresses += set_bit(bit, address, index)
        addresses = new_addresses
        index += 1
    
    return addresses

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

            mem_positions = generate_addresses(mask, mem_position)
            for pos in mem_positions:
                mem[pos] = value
    
    print(sum(mem.values()))
            

if __name__ == '__main__':
    main()
