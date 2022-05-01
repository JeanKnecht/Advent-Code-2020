from pprint import pprint
from itertools import permutations

# toevoegen input in lijst
filename = "input_jean.txt"
with open(filename, "r") as input:
    numbers =list(sorted( [int(line.strip("\n")) for line in input.readlines() if line] ))

pprint(numbers)
differences = {}
current_jolt = 0
used_volts = []

for idx in range(len(numbers)):
    next_jolt = numbers[idx]
    difference_jolt = next_jolt - current_jolt
    if difference_jolt > 3:
        # no more jolt adapters in range
        break
    
    # increase difference jolt counter wih 1
    # if key does not exist default to value 0
    differences[difference_jolt] = 1 + differences.get(difference_jolt, 0) 
    # we use teh adapter so increase joltage
    current_jolt = next_jolt

    # just for debugging keep track of all used jolts
    used_volts.append( (next_jolt, difference_jolt))

if len(used_volts) > 0:
    # last adapter adds a +3
    differences[3] = 1 + differences.get(3, 0) 


pprint(used_volts)
pprint(differences)

group_results = [differences.get(1, 0) , differences.get(3, 0) ]
group_result = differences.get(1, 0) * differences.get(3, 0)
print(f"{filename} {group_results} answer: {group_result}")

if filename == "input_test.txt":
    assert group_result == 35, "algorithm failed in " + filename
elif filename == "input_test2.txt":
    assert group_result == 220, "algorithm failed in " + filename
elif filename == "input_serge.txt":
    assert group_result == 1885, "algorithm failed in " + filename
elif filename == "input_jean.txt":
    assert group_result == 2482, "algorithm failed in " + filename