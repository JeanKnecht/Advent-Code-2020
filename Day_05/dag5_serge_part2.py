from datetime import datetime
from pprint import pprint
# Regular Expression 
import re
# from math import max
# from collections import list


#toevoegen input in lijst
filename = "input_serge.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    lines = [line.strip('\n').strip() for line in input.readlines()]


seat_regex = "^((F|B){7}(L|R){3})$"
seat_pattern = re.compile(seat_regex)
check_format = lambda value: True if re.search(pattern=seat_pattern, string=value) else False

max_seat_id = -1

existing_seat_ids = []

def calculate_seat_id(seat_string: str):
    if check_format(seat_string):
                         # alterntive of current algorith is following bit-wise operations
        row_min = 0      # 0000 0000
        row_max = 127    # 0111 1111
        row_step = 128   # 1000 0000 -> 0111 1111 and this with min or max depending on char, then roll shift right
        column_min = 0   # 0000 0000
        column_max = 7   # 0000 0111
        column_step = 8  # 0000 1000 -> 1111 0111 and this with min or max depending on char, then roll shift right

        for char in seat_string:
            if char == 'B':
                row_step /= 2
                row_min += row_step

            elif char == 'F':
                row_step /= 2
                row_max -= row_step

            elif char == 'R':
                column_step /= 2
                column_min += column_step
                
            elif char == 'L':
                column_step /= 2
                column_max -= column_step

        return int(row_max * 8 + column_min)  # seat_id

    # for invalid lines
    return -1


line_count = len(lines)
for line in lines:

    seat_id = calculate_seat_id(line)

    if seat_id != -1: # valid
        existing_seat_ids.append(seat_id)
        max_seat_id = max([seat_id, max_seat_id])


print(f"{filename} max seat id is: {max_seat_id}")

my_seat_ids = []
counter = 0
existing_seat_ids = list(sorted(existing_seat_ids))
# pprint(existing_seat_ids)

# volgende werkt wel maar kan eenvoudiger, zie na comments
# import itertools
# for BF in list(itertools.product('BF', repeat=7)):
#     for LR in list(itertools.product('LR', repeat=3)):

#         counter += 1

#         seat_id_tuple = BF + LR
#         seat_id_string = "".join(seat_id_tuple)
        
#         seat_id = calculate_seat_id(seat_id_string)

#         if seat_id not in existing_seat_ids:
#             my_seat_ids.append(seat_id)

# print(f"{filename} {counter} possible seat ids from {len(existing_seat_ids)} reservation: ")
# pprint(my_seat_ids)

# my seat id
result2 = []
for idx in range(min(existing_seat_ids), max(existing_seat_ids)):
    if not idx in existing_seat_ids:
        result2.append(idx)
print(filename, "my seat is", result2)