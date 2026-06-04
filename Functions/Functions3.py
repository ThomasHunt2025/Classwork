animals = [] 

def animal(): 
    for i in range(5):
        animal = input('Enter an animal: ')
        animals.append(animal) 

def length(): 
    for animal in animals: 
        print(animal.capitalize(), len(animal), 'characters')

animal()
print()
length() 