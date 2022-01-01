file_name = './input.txt'
fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

valid_count = 0
curr_passport = set()

def is_valid_passport(passport: set) -> bool:
    # Set operation, subtract the required fields by present fields
    # Empty set == False == Valid Passport -> Return true
    return not bool(fields - passport)

# Determine if a str can be converted to a num
def _is_number(num_str, base=10):
    try:
        int(num_str, base)
        return True
    except ValueError:
        return False

# Determine if a string is a number within the min/max range (inclusive)
def _is_in_range(num_str, min_val, max_val):
    if _is_number(num_str):
        val = int(num_str)
        return val >= min_val and val <= max_val

    return False
    

# four digits; at least 1920 and at most 2002.
def is_valid_byr(byr):
    return _is_in_range(byr, 1920, 2002)

# four digits; at least 2010 and at most 2020.
def is_valid_iyr(iyr):
    return _is_in_range(iyr, 2010, 2020)

# four digits; at least 2020 and at most 2030.
def is_valid_eyr(eyr):
    return _is_in_range(eyr, 2020, 2030)

# a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
def is_valid_hgt(hgt):
    if len(hgt) > 2:
        unit = hgt[-2:]
        num = hgt[:-2]
        if unit == 'cm':
            return _is_in_range(num, 150, 193)
        elif unit == 'in':
            return _is_in_range(num, 59, 76)
    
    return False

# a `#` followed by exactly six characters 0-9 or a-f.
def is_valid_hcl(hcl):
    if len(hcl) == 7:
        if hcl[0]=='#':
            # Verify that str is a hex val (base 16)
            return _is_number(hcl[1:], 16)
    
    return False

# exactly one of: amb blu brn gry grn hzl oth.
def is_valid_ecl(ecl):
    valid_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    return ecl in valid_colors

# a nine-digit number, including leading zeroes.
def is_valid_pid(pid):
    return len(pid) == 9 and _is_number(pid)


for line in open(file_name):
    # Get key/val pairs
    key_vals = line.strip().split()

    # Check for empty line (end of passport)
    if not key_vals:
        # Check if passport is valid
        if is_valid_passport(curr_passport):
            valid_count += 1
        
        # Reset curr passport
        curr_passport = set()
    else:
        for key_val in key_vals:
            key, val = key_val.split(":")

            # Check if that val is valid for the key type
            # Eval statement cuz I'm lazy
            if key in fields and eval(f'is_valid_{key}("{val}")'):
                # Only add key to pssport if val was legit
                curr_passport.add(key)  

if is_valid_passport(curr_passport):
    valid_count += 1

print(valid_count)

