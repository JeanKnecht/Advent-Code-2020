from datetime import datetime

slopes = ["1-1", "3-1", "5-1", "7-1", "1-2"]

filename = "input_jean.txt"
with open(filename, "r") as input:
    # read file and split the 4 values into the tuple (min, max, character, string)
    lines = [line.strip('\n')for line in input.readlines()]

# row_nr = 0
x = 0
y = 0

product = 1

lijst_bomen = []

slope_nummer = 0

bomen = 0
lengte_lijn = len(lines[0])

lambda_xy = lambda slope, value: int(slope.split("-")[value])
#lambda_y = lambda slope: int(slope.split("-")[1])

while y < len(lines[1:]):
    y += lambda_xy(slopes[slope_nummer], 1)
    list_char = [char for char in lines[y]]

    x += lambda_xy(slopes[slope_nummer], 0)

    if x >= lengte_lijn:
        x -= lengte_lijn
    if  list_char[x] == '#': # is boom
        bomen += 1

    if y == len(lines[1:]):
        lijst_bomen.append(bomen)
        bomen = 0
        y = 0
        x = 0
        slope_nummer += 1
    if slope_nummer == len(slopes):
        break

print(f"{filename} aantal bomen:", lijst_bomen)

for bomen in lijst_bomen:
    product = product * bomen

print(f"Het product van alle bomen = {product}")
