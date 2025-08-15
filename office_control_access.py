import os

def request_current_time():
    try:
        return int(input('Inform the current time in hours (0h-24h): '))
    except Exception as e:
        print(f'An error occurred {e}')
def validate_current_time(time):
    try:
        if(8 <= time <= 18):
            print('Access allowed')
        else:
            print('Access denied')
    except Exception as e:
        print(f'An error occurred {e}')

def main():
    os.system('cls')
    validate_current_time(request_current_time())

if __name__ == '__main__':
    main()
