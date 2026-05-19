'''This code implement a user defined function call calc()
-Adds 6 numbers and outputs total and average
'''
def getnum():
    '''this function aloows the user to enter a single number and returns
    the value'''
    num = int(input('Enter a number: '))
    return num
   


def calc():
    ''' this function inputs 6 numbers and does sum and avg calculations'''
    total = 0
    # get 6 inputs from user
    for i in range(6):
        mynum = getnum()
        total = total + mynum # calculate sum
 
    # cal average1

    avg = total/6

    return total,avg



# main routine
print(calc())
# output calculations