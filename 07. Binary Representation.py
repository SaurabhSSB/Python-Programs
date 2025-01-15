"""
Take input from the user and print it's binary
"""

def binary(a:int)-> int: # Binary representation as int
    """
    Calculate the binary of the given integer number
    """
    return(bin(a))

# try- except to deal with the potential ValueError input from the user
try:
    # Enter the number
    int_: int= int(input("Enter number:- "))

    # Converting to binary using the binary function
    bin_: int= binary(int_)
    
    # Print the binary of the given integer
    print(f"The binary number of {int_} is {bin_}")

except ValueError as e:
    print(f"Error: {e}")    