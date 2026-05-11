composerlist = ['Mozart W.A', '5th symp', 1791,
                'Bach J.S', 'starry night', 1750,
                'Tupac Shakur', 'California.L', 1996]

count = 0
 

print(f'Artist\t\t Title\t\t Year\t\t')

for index in range(0, len(composerlist), 3): 
     print(composerlist[index], "\t",
          composerlist[index+1], "\t",
          composerlist[index+2])  
print()
print('for in range() above') 
print() 

print('Artist\t\tTitle\t\tYear')

count = 0

for data in composerlist:
    print(data, end="\t")
    count += 1

    if count % 3 == 0:
        print()

print()
print('for data in list above')