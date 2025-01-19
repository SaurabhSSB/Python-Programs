"""
This module provides functionality to track and identify the month of an expense based on its amount.
"""
expense_list: list[int]= [2340, 2500, 2100, 3100, 2980]
month: list[str]= ["January", "February", "March", "April", "May"]

def expense_tracker(expense_amnt: int)->str:
    """
    This function finds the month in which an expense occurred based on the amount.
    :param expense_amnt: The expense amount to search for.
    :return: The name of the month if found or 'not found' if the amount does not match any recorded expenses.
    """
    for i in range(len(expense_list)):
        # Check if the current expense matches the input amount
        if expense_list[i]== expense_amnt:
            return month[i]
    return "not found"

# Using try-except to handle potential ValueError from user input
try:
    # Enter the expense amount
    expense: int= int(input("Enter the expense amount: "))

    # Finding the month in which the expense occured using expense_tracker function
    expense_month: str= expense_tracker(expense)

    # Printing the result if month not found
    if expense_month== "not found":
        print(f"Failed to find the expense month.")

    # Printing the result if month is found
    else:
        print(f"The expense was {expense} on {expense_month}")

except ValueError as e:
    print(f"Error: {e}")