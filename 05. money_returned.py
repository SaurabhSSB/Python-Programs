'''
This module calculates the money to be returned given money paid, quantity purchased and price of commodity.
'''

def rtrn(a: float,b: int,c: float)-> float:
    '''
    Calculates the money to be returned given money paid, quantity purchased and price of commodity.
    
    Args:
        a(float): Money paid
        b(int): Quantity purchased
        c(float): Price of commodity

    Returns:
        float: Money to be returned
    '''
    return ( a - ( b * c ) )

try:
    # Enter the amount of money paid
    a: float= float(input("Enter the amount of money paid:- "))
    
    # Enter the quantity purchased
    b: int= int(input("Enter the quantity purchased:- "))
    
    # Enter the price of commodity
    c: float= float(input("Enter the price of commodity:- "))

    if(a < b*c):
        raise ValueError(f"Pay {b*c-a} more.")

    # Calculating the amount to be returned using rtrn function
    d: float= rtrn(a, b, c)
    
    # Printing the amount to be returned
    print(f"Amount to be returned is {d}")

    
except ValueError as e:
    print(f"Error: {e}")