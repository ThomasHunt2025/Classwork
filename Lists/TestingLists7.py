paragraph = input('Enter a paragraph: ')
sentences = paragraph.split('.')    

count = 0
for sentence in sentences:
    words = sentence.split()
    for word in words:
        if word.isupper():
            count += 1 

print('Uppercase words:', count) 
