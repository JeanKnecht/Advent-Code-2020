##################################
filename = "input_jean.txt"

with open(filename, "r") as input:
    lijst_string = input.read()
    lijst_id = (lijst_string.split("\n\n"))

##################################

valid_counter = 0

def hoogte(hoogte):
    if len(hoogte) < 3:
        return False
    elif hoogte[-2:] == "cm":
        if 150<=int(hoogte[:-2])<=193:
            return True
        else:
            return False
    elif hoogte[-2:] == "in":
        if 59<=int(hoogte[:-2])<=76:
            return True
        else:
            return False
    else:
        return False

def hair(color):
    code = len(color[1:])
    if color[0] == "#" and code == 6:
        for char in color[1:]:
            if char not in "0123456789abcdef":
                return False
        return True
    else:
        return False

def eye(color):
    policy = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return color in policy

def pid(code):
    if len(code) == 9:
        for char in code:
            if char not in "0123456789":
                return False
        return True
    else:
        return False


for id in lijst_id:
    policy = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    elements = ((id.replace("\n", " ")).split(" "))
    print(elements)
    for element in elements:
        if element == "":
            continue
        key = element.split(":")[0]
        value = (element.split(":")[1])
        #print(value)
        if key == "byr" and (1920<=int(value)<=2002):
            policy.remove(key)
        elif key == "iyr" and (2010<=int(value)<=2020):
            policy.remove(key)
        elif key == "eyr" and (2020<=int(value)<=2030):
            policy.remove(key)
        elif key == "hgt":
            if hoogte(value) == True:
                policy.remove(key)
        elif key == "hcl":
            if hair(value) == True:
                policy.remove(key)
        elif key == "ecl":
            if eye(value) == True:
                policy.remove(key)
        elif key == "pid":
            if pid(value) == True:
                policy.remove(key)

        #print(policy)
    if not policy:
        print("list is empty so its valid")
        valid_counter += 1
    elif len(policy) == 1 and policy[0] == "cid"  :
        print(f"only the cid key is not included so its valid")
        valid_counter += 1
    else:
        print(f"list is not empty, its concludes {str(policy)}")
print(valid_counter)
