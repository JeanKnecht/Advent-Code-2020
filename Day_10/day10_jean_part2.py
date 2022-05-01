from copy import deepcopy

filename = "input_test.txt"

with open(filename, "r") as input:
    joltages = sorted([int(dx1.strip("\n")) for dx1 in input.readlines()])
    joltages.append(joltages[-1]+3)
    joltages.insert(0,0)

#What is the total number of distinct ways you can arrange the adapters to
#connect the charging outlet to your device?

#[1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]

# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)