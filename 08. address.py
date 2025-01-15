''' 
This module prints address in seperate line using + operator and f- string given street, city and country 
'''

def address_plus(a: str, b: str, c: str)-> str:
    """
    Concatenate street, city, and country into an address string using the + operator.

    Args:
        a (str): The street name.
        b (str): The city name.
        c (str): The country name.

    Returns:
        str: A formatted address string with each line separated by a newline.
    """
    return ( a + "\n" + b + "\n" + c )

def address_fstring(a: str, b: str, c: str)-> str:
    """
    Concatenate street, city, and country into an address string using the f- string operator.

    Args:
        a (str): The street name.
        b (str): The city name.
        c (str): The country name.

    Returns:
        str: A formatted address string with each line separated by a newline.
    """
    return(f"{a}\n{b}\n{c}\n")

# try- except for handling potential KeyboardInterrupt form user
try:
    # Enter street name
    street: str= input("Enter street name:- ")    

    # Enter city name 
    city: str= input("Enter city name:- ") 

    # Enter country name 
    country: str= input("Enter country name:- ")

    # Printing address in seperate line using + operator using function address_plus
    print(address_plus(street, city, country))

    # Printing address in seperate line using f- string operator using function address_fstring
    print(address_fstring(street, city, country))

except KeyboardInterrupt as e:
    print(f"Error: Program interrupted by user.")