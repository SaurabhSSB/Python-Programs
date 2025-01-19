"""
This module provides functionality for printing an increasing triangle pattern of asterisks based on user input.
"""

def pattern(start: int,up_to: int)-> None:
    """
    This function prints an increasing triangle pattern of asterisks.
    :param start: Lower limit of the range for the pattern
    :param up_to: Upper limit of the range for the pattern
    :return: None
    """
    for i in range(start, up_to + 1, 1):
        # Loop through numbers from start to up_to, printing increasing rows of asterisks
        print("*"*i)

# Using try-except to deal with potential ValueError from the user.
try:
    # Enter the lower limit
    lower_limit: int= int(input("Enter the lower limit:- "))

    # Enter the upper limit
    upper_limit: int= int(input("Enter the upper limit:- "))

    # Printing the function using pattern function
    pattern( lower_limit, upper_limit)

except ValueError as e:
    print(f"Error: {e}")