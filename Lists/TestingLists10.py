sentence = input('Enter a sentence: ') 
words = sentence.split() 

print('Words in the sentence: ', len(words))


all_capitals = 0
title_capitals = 0 

for word in words:
    if word.isupper():
        all_capitals += 1 
    elif word.istitle():
        title_capitals += 1 

print('All capital words:', all_capitals)
print('Words starting with a capital letter:', title_capitals)