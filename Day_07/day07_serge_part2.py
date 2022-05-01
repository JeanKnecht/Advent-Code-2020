from pprint import pprint

# toevoegen input in lijst
filename = "input_test.txt"
filename_dot = filename.replace("txt", "dot")
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    raw = input.read().replace("contain", "=").replace("bags", "bag").replace("bag", "").replace(".", "")
raw = raw.replace(" ", "")

# change big text line into array by key_bag
lines = raw.strip('\n').replace(" ", "").split('\n')
replacements = {line.split("=")[0]: line.split("=")[1].replace("noother", "0noother").split(",") for line in lines}

# build dictionary with bag as key and bags it contains as value array
repl_dict = {}
for key, values in replacements.items():
    value_list = []
    for value in values:
        value_qty = value[0]
        value_name = value[1:]
        value_list.append((int(value_qty), value_name))
    repl_dict[key] = value_list
pprint(repl_dict, indent=4, compact=False, width=50)

# recursive calculation of bags
def lookup(element: tuple):
    qty, name = element
    # stop condition
    if name == "noother":
        return 0

    results = []
    bags = repl_dict[name]
    for bag in bags:
        bag_qty, _= bag
        lookup_qty = lookup(bag)
        results.append(bag_qty + (bag_qty * lookup_qty))

    return sum(results) 
    
group_result = lookup((1, "shinygold"))
print(filename, "group_result", group_result)


# testing algorithm
if filename == "input_test.txt":
    assert group_result == 32, "algorithm failed in " + filename
elif filename == "input_test2.txt":
    assert group_result == 126, "algorithm failed in " + filename
elif filename == "input_serge.txt":  # test added if we want to make changes at a later date
    assert group_result == 108636, "algorithm failed in " + filename


# with open(filename_dot, "w") as output:
#     output.write("digraph MyGraph {\n")
#     for key, values in replacements.items():
#         for value in values:
#             output.write(f'{key} -> {value_name} [label= "{value_qty}"];\n')
#     output.write("}\n")
