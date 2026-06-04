citys = [] 

def enter_city():
    for i in range(5): 
        city = input('Enter a city: ')
        citys.append(city)

def characters(): 
    for city in citys:
        print(city.capitalize(), len(city), 'characters')

enter_city()
print()
characters()