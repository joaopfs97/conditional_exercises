import os

def request_number():
    try:
        return int(input('Type a whole number: '))
    except Exception as e:
        print(f'An error occurred {e}')
    
def even_number_identificator(number):
    if(number % 2 == 0):
        print('The number is even.')
    else:
        print('The number is odd.')
    
def main():
    os.system('cls')
    even_number_identificator(request_number())

if __name__ == '__main__':
    main()