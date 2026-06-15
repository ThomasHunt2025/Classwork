def getData(): 
    price = []
    total_price = 0
    discount_price = 0

    while True:
        try:
            cost = int(input('Enter the cost of the item: '))

            if cost <= 0:
                print('Erorr. Cost must be positive')
                continue

            price.append(cost)
            total_price += cost 

            item = input('Enter the item with the highest cost: ')  
            maximum_item_price = int(input('Enter the cost of the item with the highest price: '))

            if maximum_item_price >= 200:
                discount_price = maximum_item_price*0.1 
            else:
                print('That is not the maximum price')
        
        except ValueError:
            print('Recording stopped')
            break 

        print('Total cost: ', total_price)
        print('Discount: ', discount_price)
        print('Item: ', item)
        print('Cost of item', discount_price)

getData() 


            


