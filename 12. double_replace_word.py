"""
This module helps us replace multiple words in a string.
"""

def rplce (a :str )->str :
    """
    Replace a part of string and returns the modified string given a.

    Args:
        a(string)= string
    
    Return:
        string= replaced string.
    """
    return(a.replace("banana", "samose").replace("200", '10'))
    
# Using key- value pair to handle possible KeyboardInterrupt error by user.
try:
    # Entering the string
    string:str= "maine 200 banana khaye"

    # Modifying the string using rplace function
    mod_string:str= rplce(string)

    # Printing the modified string
    print(mod_string)   

except KeyboardInterrupt as e:
    print(f"Error: User terminated the program beforehand.")