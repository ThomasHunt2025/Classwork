sentence = input('Enter a sentence: ') 
words = sentence.split()

count = 0 
for word in words: 
    if word.isupper(): 
        count += 1

print('Uppercase words:', count) 