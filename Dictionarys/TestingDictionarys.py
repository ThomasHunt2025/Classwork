best_time = 0 
goal_time = 50
run_times = [] 

while True:
    user_input = int(input('How long did you run? '))
    try: 
        run_time = int(user_input)
    except ValueError:
        break

    if run_time > 0:
    run_times.append(run_time)
    
    if run_time > best_time:
        best_time > run_time

    if run_time >= goal_time: 
        print('Goal reached!')
        break 

print('Recording ended')
if run_times:
    sorted_times = sorted(run_times, reverse=True)
    print(sorted_times)
else:
    print('No valid times were entered')
