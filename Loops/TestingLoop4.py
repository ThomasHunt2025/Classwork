total = 0 

for i in range(1, 6):
    runs = int(input('Enter runs for over' + str(i) + '='))
    total += runs

    print("Total runs =", total)