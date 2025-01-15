'''
Print the number of fruits and vegetables we eat in a day given fruit_count and vegetable_count
'''

def fr_veg_count ( a: int, b: int )-> int:
    """
    Takes the number of fruits and vegetable consumed and prints it given a and b.

    Args:
        a(int): the fruit_count.
        b(int): the vegetable_count.

    Returns:
        str: output declaring the number of fruit and vegetable consumed.
    """
    return(f"The number of fruit consumed is {a} and the number of vegetable consumed is {b}.")

# Using try- except for handling possible KeybaordInterrupt error from user 
try:
    # Enter number of fruit
    fruit_count: int= int(input("Enter number of fruit:- "))
    
    # Enter number of vegetable
    vegetable_count: int= int(input("Enter number of vegetable:- "))

    # Formulating a variable containing no. of fruit and vegetable consumed using fr_veg_count function
    total_count:int= fr_veg_count(fruit_count, vegetable_count) 

    # Printing the value
    print(total_count)


except KeyboardInterrupt as e:
    print(f"Error: User terminated the program beforehand.")