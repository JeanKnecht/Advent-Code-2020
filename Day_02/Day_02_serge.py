from datetime import datetime
from pprint import pprint

EMPTY_LINES = 10

#toevoegen input in lijst
filename = "input_serge.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    lines = [line.strip('\n').replace("-", " ").replace(":", " ").replace("  ", " ").split(' ') for line in input.readlines()]
print("\n" , "=" * 40, "\n" * EMPTY_LINES)


print("Hier starten we mee .... een array van lijnen opgesplitst in de verschillende velden:")
print(lines[:10], "\n" * EMPTY_LINES)

pprint(lines[:10], indent=2)
print("\n" , "=" * 40, "\n" * EMPTY_LINES)

# convert min and max into numbers
print("ARRAY where first 2 values from each array now is an integer")
lines = [ [int(line[0]), int(line[1]), line[2], line[3]] for line in lines]
pprint(lines[:10], indent=2)
print("\n" , "=" * 40, "\n" * EMPTY_LINES)

# add count to the line
print("COUNT  line -> int")
lines = [ [line[0], line[1], line[2], line[3], line[3].count(line[2])]  for line in lines]
pprint(lines[:10], indent=2)
print("\n" , "=" * 40, "\n" * EMPTY_LINES)

# add if password is valid
print("POLICY  line -> True or False")
lines = [ [line[0], line[1], line[2], line[3], line[4], line[0] <= line[4] and line[1] >= line[4] ] for line in lines]
pprint(lines[:10], indent=2)
print("\n" , "=" * 40, "\n" * EMPTY_LINES)



# lets use a lambda because I want to have not a boolean but a number 1 or 0 if the policy if ok
# later this value will be summed up
print("LAMBDA  line -> 0 or 1")
lamda_function = lambda input_line: 1 if input_line[0] <= input_line[4] and input_line[1] >= input_line[4]  else 0

lines = [ [line[0], line[1], line[2], line[3], line[4], lamda_function(line) ] for line in lines]
pprint(lines[:10], indent=2)
print("\n" , "=" * 40, "\n" * EMPTY_LINES)

# and now the answer >>> we will sum up the 1 or 0   in line[4]
print("MAP")
count = list( map(lamda_function, lines[:10]) )
print(count)
print("\n" , "=" * 40, "\n" * EMPTY_LINES)

# and we want to sum this up to get our answer
print("ANSWER from first 10 lines")
answer = sum( map(lamda_function, lines[:10]) )
print(f"Match policy count: {answer}")
print("\n" , "=" * 40, "\n" * EMPTY_LINES)

# and we want to sum this up to get our answer
print("ANSWER ")
answer = sum( map(lamda_function, lines) )
print(f"Match policy count: {answer}")
print("\n" , "=" * 40, "\n" * EMPTY_LINES)
