filename = "input_jean.txt"

with open(filename, "r") as input:
    joltages = sorted([int(dx1.strip("\n")) for dx1 in input.readlines()])
    joltages.append(joltages[-1]+3)


def difference_joltage(value, index):
    if value == joltages[0]:
        return value
    
    return value - joltages[index-1]
        

differences = []
for val, dx2 in enumerate(joltages):
    differences.append(difference_joltage(dx2, val))


print(f"{differences.count(1)} 1'tjes * {differences.count(3)} 3'tjes = {(differences.count(1))*(differences.count(3))}")

