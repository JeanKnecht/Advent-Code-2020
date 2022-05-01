filename = "input_serge.txt"

with open(filename, "r") as input:
    raw = [int(num.strip("\n")) for num in input.readlines()]


count = 0


def check_2numbers_sum_up(number, numbers):
    for numb in numbers:
        x = number - numb

        if x != numb and x in numbers:
            return True
        else:
            continue
    return False


begin = 0
eind = 25
for dx1 in raw:
    if count >= 25:
        numbers = raw[begin:eind]
        begin += 1
        eind += 1
        if check_2numbers_sum_up(dx1, numbers):
            continue
        else:
            invalid_number = dx1
            break

    else:
        count += 1
        continue

print(invalid_number)

##############part2
stop = False
for i in range(len(raw)):
    for val, dx1 in enumerate(raw):
        
        begin = i
        eind = (i + val) + 2
        numbers = raw[begin:eind]
        #print(f"{numbers} {sum(numbers)}")

        if sum(numbers) > invalid_number:
           break

        if sum(numbers) == invalid_number:
            print(max(numbers)+min(numbers))
            print(numbers)
            print(sum(numbers))
            stop = True
            break
    if stop:
        break
