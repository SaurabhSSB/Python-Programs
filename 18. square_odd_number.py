"""
This module contains a function to print the square of all odd numbers within a specified range.
"""

def square_odd_no(lower_limit: int,upper_limit: int)->None:
    """
    This functions prints the square of all the odd numbers within the given range.
    :param lower_limit: Lower limit of the range.
    :param upper_limit: Upper limit of the range.
    :return: None the function does not return anything.
    """
    if lower_limit % 2 == 0:
        # Making sure that the range always start with an odd number
        lower_limit= lower_limit+1
    for i in range(lower_limit, upper_limit+1,2):
        print(f"Square of {i} which is an odd number is {i**2}")

# Using try-except to handle possible ValueError from the user input
try:
    # Enter the lower limit of the range
    lw_limit: int= int(input("Enter the lower limit of the range:- "))

    # Enter the upper limit of the range
    up_limit: int= int(input("Enter the upper limit of the range:- "))

    # Calling the function to print the square of all odd numbers
    square_odd_no(lw_limit, up_limit)

except ValueError as e:
    print(f"Error: {e}")