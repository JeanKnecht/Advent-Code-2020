######################################################
filename = "input_serge.txt"

with open(filename, "r") as input:
    passes = [pas.replace("\n", "") for pas in input]
######################################################

id_list = []

front = "F"
back = "B"
left = "L"
right = "R"

for code in passes:
    row = list(range(0,128))
    col = list(range(0, 8))
    char_row = [c for c in code[:7]]
    char_col = [c for c in code[7:]]
    for char in char_row:
        if char == front:
            lowest_row = row[0]
            highest_row = (int((int(row[-1])))-int(row[0]/2))+lowest_row
            row = list(range(lowest_row, highest_row+1))
            if len(row) == 1:
                row_final = int(row[0])
            elif len(row) == 2:
                row_final = int(row[1])

        if char == back:
            highest_row = row[-1]
            lowest_row = highest_row - (int((int(row[-1])-int(row[0]))/2))
            row = list(range(lowest_row, highest_row+1))

            if len(row) == 1:
                row_final = int(row[0])
            elif len(row) == 2:
                row_final = int(row[1])

    for char in char_col:
        if char == left:
            lowest_col = col[0]
            highest_col = (int((int(col[-1])-int(col[0]))/2))+lowest_col
            col = list(range(lowest_col, highest_col+1))
            if len(col) == 1:
                col_final = int(col[0])
            elif len(col) == 2:
                col_final = int(col[1])

        if char == right:
            highest_col = col[-1]
            lowest_col = highest_col - (int((int(col[-1])-int(col[0]))/2))
            col = list(range(lowest_col, highest_col+1))

            if len(col) == 1:
                col_final = int(col[0])
            elif len(col) == 2:
                col_final = int(col[1])

    id = row_final*8+col_final
    id_list.append(id)


id_sorted = sorted(id_list)
id_begin = id_sorted[0]
id_eind = id_sorted[-1]+1

id_all = list(range(id_begin, id_eind))

print(id_all)
print(id_sorted)

for ids in id_all:
    if ids not in id_sorted:
        print(f"My id is: {ids}")

print(max(id_list))
