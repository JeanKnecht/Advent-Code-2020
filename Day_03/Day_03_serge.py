from datetime import datetime
from pprint import pprint

EMPTY_LINES = 10

#toevoegen input in lijst
filename = "input_jean.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    lines = [line.strip('\n')for line in input.readlines()]

print("\n" , "=" * 40, "\n" * EMPTY_LINES)
print(lines[0], "length is:", len(lines[0]))

lines = [[char for char in line] for line in lines]
print(lines[:10])
print()
print(lines[0], "length is:", len(lines[0]))

print("\n" * 3)

# row_nr = 0
column_nr = 0
bomen = 0
lengte_lijn = len(lines[0])

print ('0  ', lines[0])

for line in lines[1:]:
    column_nr += 1

    if column_nr >= lengte_lijn:
        column_nr -= lengte_lijn

    print(column_nr, line[column_nr] ,line)



    if  line[column_nr] == '#': # is boom
        bomen += 1


print(f"{filename} aantal bomen:", bomen)
    # print(f"row {row}")



# start links bovenaan op positie 0,0

# ga 3 naar rechts ( kolom = kolom + 3)
# ga 1 naar beneden ( = volgende lijn, rij = rij + 1)

# zitten we voorbij einde van lijn ?
#    dan springgen we terug naar voor
#    nieuwe kolom positie  = kolom - lengte_lijn
