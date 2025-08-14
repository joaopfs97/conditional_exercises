import os, math
weight = 0
height = 0

def retrieve_personal_data():
    global weight, height

    try:
        weight = float(input('Type your weight: '))
        height = float(input('Type your height: '))
    except Exception as e:
        print(f'An error occurred: {e}')

def calculate_imc(weight, height):
    return weight / math.pow(height,2)

def return_classification(imc):
    try:
        if(imc < 18.5):
            print('You are underweight')
        elif(18.5 <= imc <= 25):
            print('Normal weight')
        else:
            print('You are overweight')
    except Exception as e:
        print(f'An error occurred {e}')

def main():
    os.system('cls')
    retrieve_personal_data()
    return_classification(calculate_imc(weight,height))

if __name__ == '__main__':
    main()