'''
This module calculates the area of a field given its length and breadth
'''

def area_field(a,b)-> float:
    '''
    Calculates area of the field given its length and breadth

    Args:
        a (float): Length of Field
        b (float): Breadth of Field
    
    Returns:
        float: Area of the field
    '''
    return (a * b)

try:
    # Enter the length of the field
    a: float= float(input("Enter the length of the field:- "))

    # Enter the breadth of the field
    b: float= float(input("Enter the breadth of the field:- "))

    # Calculating area using the area_field function
    c: float= area_field(a,b)

    # printing the area of the field
    print(f"The area of the field is {c}")

except ValueError as e:
    print(f"Error: {e}")