##################################
filename = "input_serge.txt"

with open(filename, "r") as input:
    lijst_string = input.read()
    lijst_id = (lijst_string.split("\n\n"))

##################################

valid_counter = 0

for id in lijst_id:
    policy = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    elements = ((id.replace("\n", " ")).split(" "))
    print(elements)
    for element in elements:
        key = element.split(":")[0]

        if key in policy:
            policy.remove(key)
        print(policy)
    if not policy:
        print("list is empty so its valid")
        valid_counter += 1
    elif len(policy) == 1 and policy[0] == "cid"  :
        print(f"only the cid key is not included so its valid")
        valid_counter += 1
    else:
        print(f"list is not empty, its concludes {str(policy)}")
print(valid_counter)
