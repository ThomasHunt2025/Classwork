def cars():
    key = input('Enter a car manufacturer (or press enter to finish): ')
    return key.strip()

car_dictionary = {}

while True:
    key = cars()

    if key == "":
        break

    key = key.title()

    if key in car_dictionary:
        car_dictionary[key] += 1
    else:
        car_dictionary[key] = 1

print('Summary of car manufacturers:')

for key in sorted(car_dictionary):
    print(f"{key}: {car_dictionary[key]}")
    