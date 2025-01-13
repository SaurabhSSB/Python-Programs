"""
This module calculates the area of a triangle given its height and base.
"""

def calculate_area(a: float, b: float) -> float:
    """
    Calculate the area of a triangle given its height and base.

    Args:
        a (float): Base of Triangle 
        b (float): Height of Triangle
    
    Returns:
        float: Calculated area of Triangle
    """
    return (a * b) / 2

# Use try-except to handle potential ValueError from user input
try:
    # Enter the Height of triangle
    a: float = int(input("Enter the height of triangle:- "))
    
    # Enter the Base of triangle
    b: float = int(input("Enter the base of triangle:- "))
    
    # Calculate area using the provided function
    c: float = calculate_area(a, b)
    
    # Print the calculated area
    print(f"The area of triangle with height {a} and base {b} is {c}.")

except ValueError:
    print("Invalid input please input numeric value for base and height.")