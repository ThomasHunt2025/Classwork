name = input("Enter full name: ")

words = name.split()
initials = ""

for word in words:
    initials += word[0].upper()

print("Initials:", initials)