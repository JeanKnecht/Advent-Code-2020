from datetime import datetime
from pprint import pprint
import re

# toevoegen input in lijst
filename = "input_serge.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    lines = [line.strip('\n').strip() for line in input.readlines()]

# pprint(lines)

# let's create a grouping function because it seems we need this frequently accross puzzles
groups = []
groups_members = []


def group_till_empty_line(lines):
    max_idx = len(lines)-1
    current_group = []
    current_group_member = []

    for idx, line in enumerate(lines):
        if line:
            current_group.extend(line)
            current_group_member.append(line)

        # did we just process the last line ....
        # or if the current pasport has ended (epty line) than we need to check if the passport is valid
        if idx == max_idx or not line:
            groups.append(current_group)
            groups_members.append(current_group_member)
            current_group = []
            current_group_member = []


group_till_empty_line(lines=lines)

# print("groups")
# pprint(groups)

# print("groups_members")
# pprint(groups_members)

group_answers = [set(group) for group in groups]
# print("group_answers")
# pprint(group_answers)

group_results = []
for idx, answers in enumerate(group_answers):
    # print("answers", answers)
    current_group_members = groups_members[idx]
    # print("\t", 'group_members', current_group_members)
    group_result = 0

    for answer in answers:
        everybody_answered = True

        for member_idx in range(len(current_group_members)):
            current_group_member = current_group_members[member_idx]
            if answer not in current_group_member:
                everybody_answered = False

        if everybody_answered:
            # if everubody answered current answer all_same will be 1 otherwise 0
            group_result += 1

    # print("\t", 'group_result', group_result)
    group_results.append(group_result)


# group_count = [len(set(group)) for group in groups]

# print("should be [3, 0, 1, 1, 1]")

# print("group_results", group_results)
print(filename, "D6 P2: sum is: ", sum(group_results))


if filename == "input_test.txt":
    assert sum(group_results) == 6, "algorithm failed in " + filename
