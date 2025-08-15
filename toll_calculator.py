import os

def request_distance():
    return int(input('Type the distance traveled in km: '))

def calculate_toll(distance):
    if(distance < 100):
        print('The toll cost is $ 10.00')
    elif(100 <= distance <= 200):
        print('The toll cost is $20.00')
    else:
        print('The toll cost is $30.00')

def main():
    os.system('cls')
    calculate_toll(request_distance())

if __name__ == '__main__':
    main()
