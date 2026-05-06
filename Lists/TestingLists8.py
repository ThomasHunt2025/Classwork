sentence = input("Enter a sentence: ") 
words = sentence.split()

uppercase_words = [] 

for word in words:
    if word.isupper(): 
        uppercase_words.append(word)

print("Uppercase words: ")
for word in uppercase_words:
    print(word)