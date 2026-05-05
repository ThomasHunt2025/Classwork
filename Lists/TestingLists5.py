Fans_list = ["John", "Emily", "Michael", "Sarah", "David"] 
New_Fans = [] 

name = input("Enter a name: ") 

if name in Fans_list: 
    print('Welcome fan!')
else:
    print("I'll add you to the New Fans list.")
    New_Fans.append(name)
    print("New Fans List:", New_Fans)