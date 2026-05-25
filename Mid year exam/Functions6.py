def check_size(): 
    size = int(input('Enter your size: '))

    if size < 10: 
        print('Small')
    
    elif size < 100:
        print('Medium') 
    else:
        print('Large')

# main routine 
check_size() 