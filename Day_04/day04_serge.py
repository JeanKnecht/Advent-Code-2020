from datetime import datetime
from pprint import pprint

EMPTY_LINES = 10

#toevoegen input in lijst
filename = "input_serge.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    lines = [line.strip('\n').strip() for line in input.readlines()]

pprint(lines)

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
for idx, line in  enumerate(lines):
    # e.g.   ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    if line:
        # split line into key, value
        values = line.split(" ")
        for value in values:

            # ve.g.alue:   ecl:gry
            key = value.split(":")[0]

            # we only add valid values to current passport list
            if key in mandatory_keys:
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
        # empty passport
        passport = []

print(filename, "valid_line_count\t", valid_line_count)
print(filename, "invalid_line_count\t", invalid_line_count)
