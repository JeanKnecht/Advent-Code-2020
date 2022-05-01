from datetime import datetime
from pprint import pprint
# Regular Expression 
import re


#toevoegen input in lijst
filename = "input_serge.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    lines = [line.strip('\n').strip() for line in input.readlines()]

# pprint(lines)

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
mandatory_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
mandatory_key_count = len(mandatory_keys)
optional_keys = ["cid"]

valid_line_count = 0
invalid_line_count = 0
passports = []
passport = []
max_idx = len(lines)-1

hcl_regex = "^#([A-Fa-f0-9]{6})$"
hcl_pattern = re.compile(hcl_regex)

ecl_regex = "^(amb|blu|brn|gry|grn|hzl|oth)$"
ecl_pattern = re.compile(ecl_regex)

pid_regex = "^([0-9]{9})$"
pid_pattern = re.compile(pid_regex)



def valid_height(key_value):
    if len(key_value) < 3:
        return False

    if key_value[-2:] in ["cm", "in"]:
        if key_value[-2:] == "cm":
            return (int(key_value[:-2]) >= 150 and int(key_value[:-2]) <= 193) 
        else: 
            return (int(key_value[:-2]) >= 59 and int(key_value[:-2]) <= 76) 

    return False

validation_rules = {
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    "byr": lambda value: int(value) >= 1920 and int(value) <= 2002,

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    "iyr": lambda value: int(value) >= 2010 and int(value) <= 2020,

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    "eyr": lambda value: int(value) >= 2020 and int(value) <= 2030,

    # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
    "hgt": lambda value: valid_height(value),

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    "hcl": lambda value: True if re.search(pattern=hcl_pattern, string=value) else False,

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    "ecl": lambda value: True if re.search(pattern=ecl_pattern, string=value) else False,

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    "pid": lambda value: True if re.search(pattern=pid_pattern, string=value) else False,

}

for idx, line in  enumerate(lines):
    # e.g.   ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    

    if line:
        
        # split line into key, value
        values = line.split(" ")
        for value in values:

            # ve.g.alue:   ecl:gry
            key = value.split(":")[0]
            key_value = value.split(":")[1]

            # we only add valid values to current passport list
            if key in mandatory_keys:
                if key_value: # empty strings are never valid
                    # if key == "pid" and key_value:
                    #     
                    print(key, key_value, validation_rules[key](key_value))

                    if validation_rules[key](key_value):
                        passport.append(key)


    # did we just process the last line .... 
    # or if the current pasport has ended (epty line) than we need to check if the passport is valid
    if idx == max_idx or not line:
        key_count = len(set(passport))

        # if unique number of keys equals mandatory fields
        if key_count == mandatory_key_count:
            valid_line_count += 1

            print('VALID\t', passport)
        else:
            invalid_line_count += 1
            print('INVALID\t', passport)

        print("")
        # empty passport
        passport = []
        
print(filename, "valid_line_count\t", valid_line_count)
print(filename, "invalid_line_count\t", invalid_line_count)
