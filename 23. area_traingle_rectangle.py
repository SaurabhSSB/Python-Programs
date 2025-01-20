"""
This module finds the area of rectangle or triangle given the dimensions and the specification of its shape.
"""

def triangle(base: float, height: float)-> float:
    """
    This function is used to find the area of triangle given its height and base.
    :param base: base of triangle
    :param height: height of triangle
    :return: area of triangle
    """
    return ( base * height ) / 2

def rectangle(length: float, breadth: float)-> float:
    """
    This function is used to find the area of rectangle given its length and breadth.
    :param length: length of rectangle
    :param breadth: breadth of rectangle
    :return: area of rectangle
    """
    return( length * breadth )

# using try-except to handle potential value-error from the user input
try:
    # Enter the first measurement
    measurement_1: float= float(input("Enter first measurement:- "))

    # Enter the second measurement
    measurement_2: float= float(input("Enter second measurement:- "))

    # Enter the shape
    shape: str= input("Enter the shape(triangle/rectangle):- ")

    # If shape is triangle
    if shape== "triangle":
        # calculating the area using triangle function
        area_shape: float= triangle(measurement_1, measurement_2)

    elif shape== "rectangle":
        # calculating the area using rectangle function
        area_shape: float= rectangle(measurement_1, measurement_2)

    else:
        raise ValueError("Only triangle or rectangle allowed.")

    # printing the area
    print(f"The area of the Figure with dimension {measurement_1} and {measurement_2} is {area_shape}")

except ValueError as e:
    print(f"Error: {e}")