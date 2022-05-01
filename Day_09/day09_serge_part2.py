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
        if window[idx1]+window[idx2] == new_number:
            value_ok = True
            window_start += 1
            break

    # if not ok
    if not value_ok:
        break

print(f"{filename}: bad number: {new_number}")

numbers = numbers[:window_start + threshold]
size = len(numbers)
value_ok = False

for idx_start in range(0, size):
    if value_ok:
        break
    for idx_end in range(idx_start+1, size):
        range_numbers = numbers[idx_start: idx_end + 1]
        range_sum = sum(numbers[idx_start: idx_end + 1])

        if range_sum == new_number:
            value_ok = True
            break


assert range_sum == new_number, "no solution was found"
assert len(range_numbers) > 1, "we should have at least 2 values"

min_max_sum = min(range_numbers) + max(range_numbers)
print(f"{filename}: values that sum up to bad number {new_number}: {range_numbers}, min: {min(range_numbers)}, max: {max(range_numbers)}, min+max: {min_max_sum}")

group_result = min_max_sum

if filename == "input_test.txt":
    assert group_result == 62, "algorithm failed in " + filename
elif filename == "input_jean.txt":
    assert group_result == 75678618, "algorithm failed in " + filename
elif filename == "input_serge.txt":  # test added if we want to make changes at a later date
    assert group_result == 245848639, "algorithm failed in " + filename
