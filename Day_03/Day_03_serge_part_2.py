from datetime import datetime
from pprint import pprint

EMPTY_LINES = 10

#toevoegen input in lijst
filename = "input_serge.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    lines = [line.strip('\n')for line in input.readlines()]

# lines = [[char for char in line] for line in lines]

results = []
lengte_lijn = len(lines[0])
 
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
opgaves = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for x_delta, y_delta in opgaves:
    bomen=0
    x = 0
    y = 0

    while y < len (lines) - 1:
        
        x += x_delta 
        y += y_delta

        line = lines[y]
        # take xth character from line, but stay inside array size (lengte_lijn)
        char  = line[x % lengte_lijn] # we nemen eenvoudig de modulus lengte_lijn

        # is het een boom ?
        if char == '#':
            bomen += 1

    print(f"{filename}    {x_delta}, {y_delta}    aantal bomen:", bomen)
    results.append(bomen)  

# controle om te zien of we voor opgave 1 (3 rechts, 1 beneden) hetzelfde resultaat hebben als in deel 1
if filename == "input_serge.txt":
    assert results[1] == 262, f"fout in het algoritme, geen 262 maar: {bomen}"

# product berekenen
product = results[0]
for idx in range(1, len(results)):
    product *= results[idx]
print(results, "answer product: ", product)