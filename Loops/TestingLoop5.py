total = 0
count = 0

mark = int(input("Enter mark (-1 to stop): "))

while mark != -1:
    total += mark
    count += 1
    mark = int(input("Enter mark (-1 to stop): "))

if count > 0:
    print("Average =", total / count)
else:
    print("No marks entered")