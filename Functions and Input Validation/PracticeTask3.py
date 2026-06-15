def study_time_analyser(): 
    study_times = []
    total_time = 0 
    longest_session = 0
    goal_reached = False 

    while True: 
        try:
            minutes  = int(input('Enter study time(minutes): '))

            if minutes < 0:
                print('Invalid Input. Study time cannot be negative')
                continue

            study_times.append(minutes)
            total_time += minutes 

            if minutes > longest_session:
                longest_session = minutes 
            
            if total_time > 500:
                print('You have reached 500 minutes or more')
                goal_reached = True
                break
        except ValueError:
            print('Invalid entry. Program stopped')
            break

    if len(study_times) > 0:
        average_time = total_time / len(study_times)
    else:
        average_time = 0

    print('Study Time Summary: ')
    print('Total Study time: ', total_time, 'minutes')
    print('Average study time:', round(average_time, 2), 'minutes')
    print("Longest study session:", longest_session, "minutes")

    if goal_reached:
        print("Goal reached: Yes")
    else:
        print("Goal reached: No")

study_time_analyser()