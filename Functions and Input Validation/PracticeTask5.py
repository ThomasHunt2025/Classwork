def getData():
    cups_list = [] 
    total_cups = 0
    best_day = 0
    goal_reached = False

    flag = True

    while flag:
        try:
            cups = int(input('How many cups of water did you drink today? '))

            if cups >= 0:
                cups_list.append(cups)
                total_cups += cups

            if cups > best_day:
                best_day = cups

            if total_cups >= 21:
                print('Congratualtions! you reached your goal of 21 cups')
                goal_reached = True
                flag = False
            else: 
                print('your input must be a positive number or 0')
        except ValueError:
            print('Please enter whole numbers only')
            flag = False
            
            if len(cups_list) > 0:
                average_cups = total_cups / len(cups_list)
            else:
                average_cups = 0

            print('Water Challenge Summary')
            print('Total cups: ', total_cups)
            print('Average cups per day', round(average_cups, 2))
            print('Best day: ', best_day)

            if goal_reached:
                print('Goal reached: Yes')
            else:
                print('Goal reaced: No')

getData() 
