# Vowel cipher
encode = {"a":"@", "e":"3", "i":"!", "o":"0", "u":"^"}
decode = {"@":"a", "3":"e", "!":"i", "0":"o", "^":"u"}

mode = input("Do you want to encode or decode? ").lower()
text = input("Enter your message: ")

result = ""

if mode == "encode":
    for char in text:
        lower_char = char.lower()
        if lower_char in encode:
            result += encode[lower_char]
        else:
            result += char

elif mode == "decode":
    for char in text:
        if char in decode:
            result += decode[char]
        else:
            result += char

else:
    print("Invalid choice")

print("Result:", result)