foods = []

def favourite_food(): 
    for i in range(5): 
        food = input('Enter a food: ')
        foods.append(food)

def characters(): 
    for food in foods: 
        print(food.capitalize(), len(food), 'characters') 


favourite_food()
print()
characters()
