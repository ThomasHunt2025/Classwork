haircut = {} 
no_haircut = {} 

for i in range(5):
    key = input('Enter a students name: ')
    ans = input('Do they need a haircut(Y/N): ').upper() 
    
    if ans == 'Y':
        value = True
        haircut[key] = value 
    
    elif ans == 'N':
        value = False
        no_haircut[key] = False 
    else:
        value = None
    
    print(haircut)

    

   
