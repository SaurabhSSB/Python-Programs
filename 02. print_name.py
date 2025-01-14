"""
Printing name as one but taking the name in three different sections.

This script prompts the user for their first, middle, and last name,
then prints the full name.
"""

def get_full_name() -> str:
    """
    Prompts the user for their first, middle, and last names and returns the full name.

    Returns:
        str: The full name composed of first, middle, and last name with spaces in between.
    """
    # Collect first name from user
    first_name: str = input("Enter First Name: ")
    
    # Collect middle name from user
    middle_name: str = input("Enter Middle Name: ")
    
    # Collect last name from user
    last_name: str = input("Enter Last Name: ")
    
    # Combine all parts of the name into one string
    full_name: str = f"{first_name} {middle_name} {last_name}"
    
    return full_name

# Call the function to get and print the full name
print(get_full_name())
