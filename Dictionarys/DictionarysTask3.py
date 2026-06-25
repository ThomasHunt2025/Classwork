'''
This program asks the user to enter a student's name and attendance percentage.
It stores the results in a dictionary and displays a summary.
'''

def get_input():
    '''Repeatedly asks for the student's name and attendance percentage.'''

    while True:
        student_name = input("Enter the student's name (or press Enter to finish): ").strip()

        if student_name == "":
            return "", None

        try:
            attendance = float(input("Enter their attendance percentage: "))

            if 0 <= attendance <= 100:
                return student_name, attendance
            else:
                print("Attendance percentage must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


student_dictionary = {}


while True:
    name, attendance = get_input()

    if name == "":
        break

    student_dictionary[name] = attendance


print("Attendance Summary")

total = 0

for name in sorted(student_dictionary):
    print(f"{name}: {student_dictionary[name]:.1f}%")
    total += student_dictionary[name]

if len(student_dictionary) > 0:
    average = total / len(student_dictionary)
    print(f"Overall average attendance: {average:.1f}%")
else:
    print("No student data entered.")