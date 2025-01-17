"""
This module helps to find whether a person's sugar level is normal or not given the sugar level.
"""

def sugar_check(sug_level: float)-> str:
    """
    This function helps decide whether a person's sugar level is normal or not given the sugar level.
    :param sug_level: Sugar level of the user
    :return:  tells whether a person sugar level is normal, high or low.
    """
    if sug_level<80:
        return "low"
    elif sug_level<= 100:
        return "normal"
    else:
        return "high"

# using try-except for handling potential ValueError from the user.
try:
    # Enter the level of sugar while fasting.
    sug_lvl_fasting: float= float(input("Enter the level of sugar while fasting:- "))

    # Deciding sugar level using sugar_check function.
    sugar_lvl_result: str= sugar_check(sug_lvl_fasting)

    # print the result
    print(f"Your sugar level is {sugar_lvl_result}")

except ValueError as e:
    print(f"Error: {e}")