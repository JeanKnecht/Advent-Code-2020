from datetime import datetime

#input
filename = "input_jean_2.txt"
input = open(filename, "r")

passwords = [ str((lijn.replace(':', '')).strip('\n')) for lijn in input.readlines() ]
#################

tijd_start = datetime.now()

valid_counter = 0
invalid_counter = 0

for dx1 in passwords:
    counter = 0
    delen = dx1.split(" ")

    letter_policy = str(delen[1])
    password = delen[2]

    cijfer_policy_1 = int((delen[0].split("-"))[0])
    cijfer_policy_2 = int((delen[0].split("-"))[1])+1

    for letter in password:
        if letter == letter_policy:
            counter += 1

    if counter in range(cijfer_policy_1,cijfer_policy_2):
        valid_counter += 1
    elif counter not in range(cijfer_policy_1,cijfer_policy_2):
        invalid_counter += 1

tijd_einde = datetime.now()
print(f"In total there are {len(passwords)} passwords\n")
print(f"There are {valid_counter} valid passwords \n")
print(f"There are {invalid_counter} invalid passwords \n")
print(f"Duration: {str(tijd_einde-tijd_start)} \n")
