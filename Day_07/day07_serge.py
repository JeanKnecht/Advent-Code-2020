from datetime import datetime
from pprint import pprint
import re
from copy import deepcopy

# toevoegen input in lijst
filename = "input_jean.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    raw = input.read().replace("contain", "=").replace("bags", "bag").replace(".", "")
raw = raw.replace(" ", "")

#
# build our own translation based on input
#
translations = {
    "shinygoldbag": "G",
    "nootherbag": ""
}

# translation dict: build all keys with a value xNUMBER_
next_key_id = 0
for line in raw.split("\n"):
    if line:
        key, value = line.split('=')
        if key not in translations:
            translations[key] = "x" + str(next_key_id) + "_"
            next_key_id += 1

# translate all input values based on translation dict
for key, value in translations.items():
    raw = raw.replace(key, value)

# change big text line into array by key_bag
lines = raw.strip('\n').replace(" ", "").split('\n')
pprint(lines)

# multiply number of bags in value
replacements = {}
for line in lines:
    parts = line.split("=")
    key = parts[0]
    v = []
    values = parts[1].split(",")
    for value in values:
        if value:
            v.extend(value[1:])
    v = "".join(v)
    replacements[key] = v

# we don't want to replace G bags  becaue we want to count them
# so remove it from key list so that we will not replace G by its content
del replacements["G"]
pprint(replacements)


# apply replacements till there are no more changes
repl2 = deepcopy(replacements)
first_run = True
while repl2 != replacements or first_run:

    # thy shall not change thee object while iterating it !
    replacements = deepcopy(repl2)
    first_run = False

    for key2, value2 in repl2.items():
        print(key2, flush=True)
        for key1, value1 in replacements.items():
            value2 = value2.replace(key1, value1)  # .replace(";;", ";")
        repl2[key2] = value2


# now count the number of Gs in it bag type
def has_G(line): return 1 if 'G' in line else 0
group_results = [has_G(value) for key, value in repl2.items()]

print("group_results", group_results)
print(filename, "D7 P1: sum is: ", sum(group_results))


if filename == "input_test.txt":
    assert sum(group_results) == 4, "algorithm failed in " + filename
elif filename == "input_serge.txt":  # test added if we want to make changes at a later date
    assert sum(group_results) == 101, "algorithm failed in " + filename
