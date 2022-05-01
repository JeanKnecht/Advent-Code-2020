from datetime import datetime
from pprint import pprint
# Regular Expression
import re
# from math import max


#toevoegen input in lijst
filename = "input_serge.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    lines = [line.strip('\n').strip() for line in input.readlines()]


seat_regex = "^((F|B){7}(L|R){3})$"
seat_pattern = re.compile(seat_regex)
check_format = lambda value: True if re.search(pattern=seat_pattern, string=value) else False

max_seat_id = -1

for line in lines:
    # check if input is valid
    if check_format(line):
                         # alterntive of current algorith is following bit-wise operations
        row_min = 0      # 0000 0000
        row_max = 127    # 0111 1111
        row_step = 128   # 1000 0000 -> 0111 1111 and this with min or max depending on char, then roll shift right
        column_min = 0   # 0000 0000
        column_max = 7   # 0000 0111
        column_step = 8  # 0000 1000 -> 1111 0111 and this with min or max depending on char, then roll shift right

        for char in line:
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

            seat_id = int(row_max * 8 + column_min)

        max_seat_id = max([seat_id, max_seat_id])

        print(f"{line} valid row {row_max:.0f} , column {column_min:.0f}, seat_id {seat_id:.0f}")

    else:
        print(line, "invalid")


print("""\nwe should get:
    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.
""")

print(f"{filename} max seat id is: {max_seat_id}")
