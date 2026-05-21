weathers = []

def check_weather(): 
    weather = int(input('Enter a tmeperature: '))
    
    if weather > 25:
        print('Hot')
    
    elif weather >= 15:
        print('Warm') 
    
    elif weather < 15: 
        print('Cold')

check_weather()

