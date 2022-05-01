from datetime import datetime

#toevoegen input in lijst
filename = "input_serge.txt"
input = open(filename, "r")
numbers = [int(lijn) for lijn in input.readlines()]
numbers = sorted(numbers)

print(numbers)
tijd_start = datetime.now()

counter = 0
for idx1 in range(0, len(numbers)):
    # idx1 = 1

    for idx2 in range(idx1 + 1, len(numbers)):

        for idx3 in range(idx2 + 1, len(numbers)):

            counter += 1

            if numbers[idx1] + numbers[idx2] + numbers[idx3]  == 2020:
                print(f"\nSolution: for {filename} ")
                print(f"{numbers[idx1]} + {numbers[idx2]}  +  {numbers[idx3]} = {numbers[idx1] + numbers[idx2] + numbers[idx3]}")
                print(f"{numbers[idx1]} * {numbers[idx2]}  *  {numbers[idx3]} = {numbers[idx1] * numbers[idx2] * numbers[idx3]}")

            elif numbers[idx1] + numbers[idx2] + numbers[idx3] > 2020:
                break

tijd_einde = datetime.now()

old_count = len(numbers) ** 3
new_count = counter
improvement = (old_count * 1.0) /  (new_count * 1.0)
print('\nStatistics:')
print(f"The old way we would solve this puzzel with {old_count} calculations.")
print(f"The new way we solved this puzzel with {new_count} calculations. This is an improvement of {improvement:.2f} %")

print(f"Duration: {str(tijd_einde-tijd_start)} \n")
