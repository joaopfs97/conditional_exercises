import os, math
weight = 0
height = 0

def retrieve_personal_data():
    '''
    This function is responsible to retrieve the weight(kg) and height(m) of the user
    '''
    global weight, height

    try:
        weight = float(input('Type your weight (kg): '))
        height = float(input('Type your height (m): '))
    except Exception as e:
        print(f'An error occurred: {e}')

def calculate_imc(weight, height):
    '''
    This function is responsible to calculate the IMC with the informed data\n
    inputs: float - weight, float height\n
    outputs: float - imc value
    '''
    return weight / math.pow(height,2)

def return_classification(imc):
    '''
    This function is responsible to classify the user according to the imc value
    '''
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