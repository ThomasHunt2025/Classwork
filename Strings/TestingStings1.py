sentence = input("Enter a sentence: ").lower()

vowels = "aeiou"
total = 0

counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letter in sentence:
    if letter in vowels:
        total += 1
        counts[letter] += 1

print("Total vowels:", total)
print("A:", counts["a"])
print("E:", counts["e"])
print("I:", counts["i"])
print("O:", counts["o"])
print("U:", counts["u"])