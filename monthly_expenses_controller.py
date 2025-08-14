import os
limit = 3000

def retrieve_month_cost():
    try:
        return float(input('Type the total expenses for the month (R$): '))
    except Exception as e:
        return f'An error occurred {e}'
def valuate_cost(expenses):
    global limit
    if expenses > limit:
        print(f'Atention! you have exceeded the budget limit!')

def main():
    os.system('cls')
    valuate_cost(retrieve_month_cost())

if __name__ == '__main__':
    main()