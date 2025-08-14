# The list of global variables
number_of_apples = 0
number_of_bananas = 0
best_selling = ''
def request_product_data():
    '''
    This function is responsible to request to the user the number of apples and bananas sold
    '''
    global number_of_apples
    global number_of_bananas

    number_of_apples = int(input('Type the number of apples sold: '))
    number_of_bananas= int(input('Type the number of bananas sold: '))
def calculate_best_selling_product():
    '''
    This function is responsable to calculate the best selling product
    '''
    global best_selling 

    best_selling = 'Apples' if number_of_apples > number_of_bananas else 'Bananas'
def show_best_selling_product():
    '''
    This function is responsible to show the best selling product on terminal
    '''
    print(f'The {best_selling} had more sales')

def main():
    request_product_data()
    calculate_best_selling_product()
    show_best_selling_product()

if __name__ == '__main__':
    main()