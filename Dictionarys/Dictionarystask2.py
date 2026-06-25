'''
This program repeatedly asks the user to enter a car manufacturer
'''


def get_car():
    '''Repeatedly ask the user to enter the car manufacturer name'''
    key = input('Enter a car manufacturer (or press enter to finish): ').title()
    return key.strip()

car_dictionary = {}

flag = True
while flag:
    key = get_car()
    '''If the user presses enter, the code stops'''
    '''Uses a dictionary to store how many times each car brand was entered'''
    if key == '':
        flag = False
    elif key in car_dictionary:
        car_dictionary[key] += 1
    else:
        car_dictionary[key] = 1

'''Prints a summary showing each car brand and how many times it was entered'''
print('Summary of car manufacturers:')

for key in sorted(car_dictionary):
    print(f"{key}: {car_dictionary[key]}")
    
