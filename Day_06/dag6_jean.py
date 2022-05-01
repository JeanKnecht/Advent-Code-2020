#####################################
filename = "input_serge.txt"

with open(filename, "r") as input:
    groepen = input.read()
    antwoorden = groepen.split("\n\n")
#####################################

count_char = []

def get_unique_char(word):
    count = 0
    for char in word:
        if count == 0:
            unique_list.append(char)
            count += 1
            continue

        if char not in unique_list:
            unique_list.append(char)
        else:
            continue

    count_char.append(len(unique_list))

for antwoord in antwoorden:
    unique_list = []
    previous_char = []
    antwoord = antwoord.replace("\n", "")
    get_unique_char(antwoord)

print(sum(count_char))
