from datetime import datetime
from pprint import pprint
# Regular Expression 
import re
# from math import max
# from collections import list


#toevoegen input in lijst
filename = "input_serge.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    lines = [line.strip('\n').strip() for line in input.readlines()]

# pprint(lines)

# let's create a grouping function because it seems we need this frequently accross puzzles
groups = []
def group_till_empty_line(lines):
    max_idx = len(lines)-1
    current_group = []
    for idx, line in  enumerate(lines):
        if line:
            current_group.extend(line)

        # did we just process the last line ....
        # or if the current pasport has ended (epty line) than we need to check if the passport is valid
        if idx == max_idx or not line:
            groups.append(current_group)
            current_group = []

group_till_empty_line(lines=lines)
# pprint(groups)
group_count = [len(set(group)) for group in groups]

# print(group_count)
print(filename, "sum is: ", sum(group_count))

if filename == "input_test.txt":
    assert sum(group_count) == 11, "algorithm failed in " + filename