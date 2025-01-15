'''
A module that prints substrings by string slicing and negative index given string.
'''

def str_slicing(a:str)-> str:
    '''
    Print substring using string slicing method.

    Args:
        a(str): String from user.

    Returns:
        str: Substring using string slicing.
    '''
    return a[6:14]

def str_index(a:str)-> str:
    '''
    Print substring using negative index method.

    Args:
        a(str): String from user.

    Returns:
        str: Substring using negative index.
    '''
    return a [ -3 : ]

# using try- except to handle possible KeyboardInterrupt form user
try:
    # Enter the string
    string: str= "Earth revolves around the sun"

    # Calculate Substring using str_slicing function
    b: str= str_slicing(string)

    # Calculate Substring using str_index function
    c: str= str_index(string)

    # Print Substring found using string slicing
    print(f"{b} is substring of {string} calculated using string slicing")

    # Print Substring found using negative index
    print(f"{c} is substring of {string} calculated using negative index")

except KeyboardInterrupt as e:
    print(f"Error: The user interrupted the program.")