from pprint import pprint
from itertools import permutations

# toevoegen input in lijst
filename = "input_jean.txt"
with open(filename, "r") as input:
    numbers = [int(line.strip("\n"))for line in input.readlines() if line]

threshold = 5 if filename == "input_test.txt" else 25
window_start = 0
all_idxs = list(range(threshold))

for new_number in numbers[threshold:]:
    # check validity new_number
    window = numbers[window_start:window_start + threshold]
    value_ok = False
    for idx1, idx2 in permutations(all_idxs, 2):
        if window[idx1]+window[idx2]==new_number:
            value_ok = True
            window_start += 1
            break
    
    # if not ok
    if not value_ok:
        break

print(filename, "bad number:", new_number)
group_result = new_number

if filename == "input_test.txt":
    assert group_result == 127, "algorithm failed in " + filename
elif filename == "input_jean.txt":
    assert group_result == 542529149, "algorithm failed in " + filename
elif filename == "input_serge.txt":  # test added if we want to make changes at a later date
    assert group_result == 2089807806, "algorithm failed in " + filename

