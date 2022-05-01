################################
filename = "input_jean.txt"

with open(filename, "r") as input:
    rules = [line.strip("\n") for line in input.readlines()]

################################

# soorten bags in lijst
soorten = []
for rule in rules:
    elements = rule.split(" ")
    soorten.append(f"{elements[0]} {elements[1]}")
# lijst for howmany gold in bag
aantal = []
gold_carry = []
for rule in rules:

    if "shiny gold" in rule:
        if rule.find("shiny gold") == 0:
            aantal.append(0)
            continue
        else:
            # x = rule[int(rule.find("shiny gold")-2)]
            aantal.append(1)
            gold_carry.append(rule.split(" bags contain")[0])
            continue
    else:
        aantal.append(0)
# dictionnary voor hoeveel gold elke bag draagt
gold_soort = {}
for i in range(len(soorten)):
    gold_soort[soorten[i]] = aantal[i]
# dict with bags per bag
soorten_bag = {}
for i in range(len(rules)):
    soorten_lijst = []
    for soort in soorten:
        x = rules[i].split(" bags contain")[1]
        if soort in x:
            soorten_lijst.append(soort)

    soorten_bag[soorten[i]] = soorten_lijst
# dict with bags per bag en aantal
soorten_bag_x = {}
for i in range(len(rules)):
    soorten_lijst = []
    for soort in soorten:
        x = rules[i].split(" bags contain")[1]
        if soort in x:
            aantal_x = x[(x.find(soort) - 2)] 
            soorten_lijst.append(f"{aantal_x} {soort}")

    soorten_bag_x[soorten[i]] = soorten_lijst

#######################################################################
# How many bag colors can eventually contain at least one shiny gold bag?
# we hebben dus een dictionnary met de bags en of de bags al dan niet een golden dragen: gold_soort
# we hebben ook een dictionnary met de bags en de bags die daarin zitten: soorten_bag
# we hebben een lijst met soorten bags in lijst
# ""gold_carry"" = [] lijst waarin shiny kan zitten, hier dus stoppen wanneer je deze tegenkomt
# max 4 bags in andere bag

#############
##part_1#####
#############


# gold_in_bag = lambda bag: True if gold_soort[bag] == 1 else False

# checkt = 0
# checking = True

# while checking:
#     break_check = False
#     checkt = 0
#     for soort in soorten:
#         checkt += 1
#         for bag in soorten_bag[soort]:
#             if bag in gold_carry and soort not in gold_carry:
#                 break_check = True
#                 gold_carry.append(soort)
#                 break
#             else:
#                 continue
#         if break_check:
#             break
#         if checkt == len(soorten):
#             checking = False
#             break
# print(f"aantal bags is gelijk aan: {len(set(gold_carry))}")

#############
##part_2#####
#############

aantal_lambda = lambda bag: bag[0]
checking = True

lijst_soorten = []
dict_aantal = {}
checkt = 0

while checking:
    values = dict_aantal.values()
    y = sum(values)
    checkt += 1
    break_check = False
    ok = False
    for bag in soorten_bag["shiny gold"]:
        name = f"shiny gold={bag}"
        if name not in lijst_soorten:
            lijst_soorten.append(name)
            place = soorten_bag["shiny gold"].index(bag)
            x = aantal_lambda(soorten_bag_x["shiny gold"][place])
            dict_aantal[name] = int(x)

            ok = True
            break

    if ok:
        continue


    for bag2 in lijst_soorten:
        key = dict_aantal[bag2]
        for bag3 in soorten_bag[bag2.split("=")[-1]]:
            name2 = f"{bag2}={bag3}"
            if name2 not in lijst_soorten:
                lijst_soorten.append(name2)
                place = soorten_bag[bag2.split('=')[-1]].index(bag3)
                x = aantal_lambda(soorten_bag_x[bag2.split('=')[-1]][place])
                dict_aantal[name2] = int(x)*key
                
                break_check = True
                break

        if break_check:
            break

        if checkt == 1000:
             checking = False
             break

values = dict_aantal.values()
print(dict_aantal)
print(sum(values))