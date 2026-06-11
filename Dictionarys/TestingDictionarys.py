best_time = 0
goal_time = 60
hold_times = []

def breath_time():
    best_time = True
    while True:
        user_input = input('How long can you hold your breath? ')
        
        try:
            hold_time = int(user_input)
        except ValueError:
            break

        if hold_time > 0:
            hold_times.append(hold_time)

        if hold_time > best_time:
            best_time = hold_time

        if hold_time >= goal_time:
            print('Goal reached!')
            print('Recording ended')
            break

breath_time()