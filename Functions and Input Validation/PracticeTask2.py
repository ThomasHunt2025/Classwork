def cricket_score_tracker():
    scores = []
    total_score = 0 
    highest_over = 0 

    while True:
        try: 
            runs = int(input('Enter runs scored in the over: '))

            if runs < 0:
                print('Invalid input. Score cannot be negative.')
                continue

            scores.append(runs)
            total_score += runs

            if runs > highest_over:
                highest_over = runs

            if total_score >= 150:
                print('Goal reached! Total score is 150 or more')
        
        except ValueError:
            print('Non-number entered. recording stopped')
            break 

        print('Cricket score summary: ')
        print('Total score: ', total_score)
        print('Highest Over: ', highest_over)
        print('number of overs recorded: ', len(scores))

cricket_score_tracker() 

            