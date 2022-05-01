from pprint import pprint
import copy
acc = 0

filename = "input_jean.txt"
with open(filename, "r") as input:
    raw = [command.replace("\n", "") for command in input.readlines()]

commands = {}
for i in range(len(raw)):
    place = f'{i+1  }.'
    command = (raw[i]).split(" ")[0]
    value = int((raw[i]).split(" ")[1])

    commands[place+command] = value

new_commands = copy.deepcopy(commands)
running = True
count = 0
list_runned_commands = []
list_checked_commands = []
command = lambda count: (list(new_commands.keys())[count])

def new_dict(new, old):
    key_old = commands.keys()
    values = commands.values()

    key_new = [key.replace(old, new) for key in key_old]

    new_zip = zip(key_new, values)
    new_dict = dict(new_zip)

    return new_dict

def next():
    global new_commands
    for key in list(commands.keys()):
        place = key.split(".")[0]
        old_key = key.split(".")[1]
        if old_key == "jmp" and key not in list_checked_commands:
            new_key = f"{place}.nop"
            new_commands = new_dict(new_key, key)
            list_checked_commands.append(key)
            break
        elif old_key == "nop" and key not in list_checked_commands:
            new_key = f"{place}.jmp"
            new_dict(new_key, key)
            new_commands = new_dict(new_key, key)
            list_checked_commands.append(key)
            break


while running:

    if count == len(raw):
        running = False
        continue
    
    x = command(count)
    cd = x.split(".")[1]

    if x in list_runned_commands:
        new_commands = copy.deepcopy(commands)
        list_runned_commands = []
        count = 0
        acc = 0
        next()
        continue

    else:
        list_runned_commands.append(x)

    if cd == "acc":
        acc += new_commands[x]
        count += 1
    elif cd == "jmp":
        count += new_commands[x]

    elif cd == "nop":
        count += 1

print(acc)