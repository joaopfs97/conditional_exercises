import os
monthly_income = 0
installment = 0

def request_monthly_income():
    global monthly_income

    monthly_income = int(input('Type the value of your monthly income: '))

def request_intallment_value():
    global installment

    installment = int(input('Type the installment value: '))

def loan_validation(monthly_income, installment):
    if(monthly_income < 2000):
        print('Loan denied. The monthly income is under $2000.00')
    else:
        if(installment > (monthly_income * 0.3)):
            print('Loan denied. The installment above 30% of the monthly income')
        else:
            print('Loan approved')

def main():
    os.system('cls')
    request_monthly_income()
    request_intallment_value()
    loan_validation(monthly_income, installment)

if __name__ == '__main__':
    main()