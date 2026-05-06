sentence = input("Enter a sentence: ")
words = sentence.split()

uppercase_words = [word for word in words if word.isupper()] 

if len(uppercase_words) == 0: 
    print("No uppercase words found.")
else:    
    print("Uppercase words: ", len(uppercase_words))