file_name = './input.txt'
fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

invalid_count = 0
curr_passport = set()

def is_valid(passport: set) -> bool:
    # Set operation, subtract the required fields by present fields
    # Empty set == False == Valid Passport -> Return true
    return not bool(fields - passport)

for line in open(file_name):
    # Get key/val pairs
    key_vals = line.strip().split()

    # Check for empty line (end of passport)
    if not key_vals:
        # Check if passport is valid
        if is_valid(curr_passport):
            invalid_count += 1
        
        # Reset curr passport
        curr_passport = set()
    else:
        for key_val in key_vals:
            key = key_val.split(":")[0] # Get key
            curr_passport.add(key)      # Add key to passport

if is_valid(curr_passport):
    invalid_count += 1

print(invalid_count)

