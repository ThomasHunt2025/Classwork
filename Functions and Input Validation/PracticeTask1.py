def workout_counter():
    best_set = 0
    total_reps = 0
    sets = []

    while True:
        try:
            reps = int(input("Enter reps completed in the set: "))

            if reps <= 0:
                print("Error: Reps must be greater than 0.")
                continue

            sets.append(reps)
            total_reps += reps

            if reps > best_set:
                best_set = reps
                print("Personal Best Set!")

            if total_reps >= 100:
                print("Fitness goal reached!")
                break

        except ValueError:
            print("Non-number entered. Program stopped.")
            break

    if len(sets) > 0:
        average_reps = total_reps / len(sets)

        print("Workout Summary: ")
        print("Total reps:", total_reps)
        print("Average reps per set:", round(average_reps, 2))
        print("Best set:", best_set)
        print("Sets in descending order:", sorted(sets, reverse=True))
    else:
        print("No valid sets were entered.")


workout_counter()
              