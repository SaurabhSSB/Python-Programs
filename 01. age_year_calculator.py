"""
Program to find your current age in years.

This script prompts the user for their birth year and the current year,
then calculates and displays their age.
"""

def calculate_age(birth_year: int, current_year: int) -> int:
    """
    Calculate age based on birth year and current year.

    Args:
        birth_year (int): The year the person was born.
        current_year (int): The current year.

    Returns:
        int: The calculated age in years.
    """
    if birth_year > current_year:
        raise ValueError("Birth year cannot be after the current year!")
    return current_year - birth_year

# Using try-except to handle potential ValueError from the user input
try:
    # Prompt user for birth year
    birth_year: int = int(input("Enter your birth year: "))

    # Prompt user for current year
    current_year: int = int(input("Enter the current year: "))

    # Calculate age
    age: int = calculate_age(birth_year, current_year)

    # Display age
    print(f"Your age is: {age} years")

except ValueError as e:
    print(f"Error= {e}")