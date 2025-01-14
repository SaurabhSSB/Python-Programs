'''
This module calculates the revenue given the price of commodity and quantity of commodity bought
'''

def revenue(a: float, b: int)-> float:
    '''
    Calculates the revenue given the price of commodity and qunatity of commodity bought

    Args:
        a (float): Price of commodity
        b (int): Quantity of commodity bought

    Return:
        float: Revenue 
    '''
    return ( a * b )

try:
    # Enter the price of the commodity
    a: float= float(input("Enter the price of the commodity:- "))

    # Enter the quantity of commodity bought
    b: int= int(input("Enter the quantity of commodity bought:- "))

    # Calculating the revenue using revenue function
    c: float= revenue(a,b)

    # Print the revenue
    print(f"The total revenue is {c}")

except ValueError as e:
    print(f"Error: {e}")