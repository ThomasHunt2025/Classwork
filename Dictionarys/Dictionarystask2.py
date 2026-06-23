def cars():
    '''Repeatedly ask the user to enter the car manufacturer name'''
    key = input('Enter a car manufacturer (or press enter to finish): ').title()
    return key.strip()

car_dictionary = {}

flag = True
while flag:
    key = cars()
    '''If the user presses enter, the code stops'''
    if key == '':
        flag = False
        
    elif key in car_dictionary:
        car_dictionary[key] += 1
    else:
        car_dictionary[key] = 1

print('Summary of car manufacturers:')

for key in sorted(car_dictionary):
    print(f"{key}: {car_dictionary[key]}")
    
