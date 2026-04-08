text = input("Enter a word or phrase: ")

cleaned = text.lower().replace(" ", "")
reversed_text = cleaned[::-1]

if cleaned == reversed_text:
    print("It IS a palindrome because it reads the same forward and backward.")
else:
    print("It is NOT a palindrome because it changes when reversed.")