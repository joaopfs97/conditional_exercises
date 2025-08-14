import os

def report_current_temperature():
    '''
    This function is responsible to store the current temperature\n
    inputs: the user input the temperature\n
    output: the temperature informed by the user
    '''
    try:
        return float(input('Type the current temperature: '))
    except Exception as e:
        print(f'An error occurred {e}')

def validate_temperature(temperature):
    '''
    This function is responsible to validate the temperature and return an Alert if it is above 25ºC\n
    input: The temperature in ºC\n
    output: A string alert if the temperature is above 25ºC
    '''
    try:
        if(temperature > 25):
            print("ALERT! The temperature is above the permited level")
    except Exception as e:
        print(f'An error occurred {e}')

def main():
    os.system('cls')
    validate_temperature(report_current_temperature())

if __name__ == '__main__':
    main()