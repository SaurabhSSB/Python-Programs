""" 
Find the price of replacing tile at INR 500/sq. feet given the length and breadth of bathroom
"""

def price_tile(a:float, b:float)-> float:
    """
    Calculate the total cost required to replace the tile given length and breadth of the bathroom

    Args:
        a (float): The length of the bathroom
        b (float): The breadth of the bathroom

    Return:
        float: The cost required to replace tile
    """
    return ((a*b)*500)

# try- except loop to handle the potential ValueError input from the user 
try:
    # Enter the length of Bathroom
    bathroom_len: float= float(input("Enter the length of Bathroom:- "))

    # Enter the breadth of Bathroom
    bathroom_br: float= float(input("Enter the breadth of Bathroom:- "))

    # Calculating total cost of replacing tile using price_tile function
    tile_cost= price_tile ( bathroom_len , bathroom_br )
    
    # Printing the total cost of replacing tile
    print(f"The total cost of replacing the tile of the bathroom is INR {tile_cost}")

except ValueError as e:
    print(f"Error: {e}")