from pprint import pprint

#####################################
filename = "input_jean.txt"

with open(filename, "r") as input:
    groepen = input.read()
    antwoorden = groepen.split("\n\n")
pprint(antwoorden)
#####################################
counts = 0

def not_unique(word):
    print(word)
    lengte_aantal = len(antwoord)
    print(lengte_aantal)
    aantal = 0
    code = list(word)
    #code = list(set(code))
    bekeken_code = []
    print(code)
    for element in code:
        #print(f"element {element} komt {code.count(element)} keer voor")
        if element in bekeken_code:
            continue
        bekeken_code.append(element)
        if code.count(element) == lengte_aantal:
            aantal += 1

    print(f"er zijn {aantal} gelijkaardige oplossingen")

    return aantal

if antwoorden[-1] == '':
    del antwoorden[-1]

for antwoord in antwoorden:
    antwoord = antwoord.strip("\n").split("\n")
    print(antwoord)

    if antwoord[-1] == '':
        del antwoord[-1]


    if len(antwoord) == 1:
        aantal = list(antwoord[0])
        counts += len(aantal)
        continue
    else:
        string_group = ''.join(antwoord)
        print(string_group)
        counts += (not_unique(string_group))
        continue


print(f"er zijn in totaal {counts} gelijkaardige oplossingen")
