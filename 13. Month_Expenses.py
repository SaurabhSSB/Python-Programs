from typing import List

def monthly_expenses_tracker(expenses: List[int]) -> None:
    """
    This function tracks and performs operations on monthly expenses.

    :param expenses: A list containing monthly expenses in dollars.
    """
    # Extra dollars spent in February compared to January
    jan_vs_feb: int = expenses[1] - expenses[0]
    print(f"Extra dollars spent in February compared to January: {jan_vs_feb}")

    # Total expense for the first quarter of the year
    first_quarter_expense: int = sum(expenses[:3])  # Using sum for clarity and efficiency
    print(f"Total expense in the first quarter: {first_quarter_expense}")

    # Check if exactly 2000 dollars was spent in any month
    find_2000: bool = 2000 in expenses
    print(f"Was 2000 dollars spent in any month? {find_2000}")

    # Add a new expense entry for May
    expenses.append(1980)
    print(f"New expense added for May: {expenses[-1]}")

    # Adjust April's expense after returning an item for a refund
    expenses[3] -= 200
    print(f"April expense after refund: {expenses[3]}")

    # Print updated list of expenses
    print(f"Updated monthly expenses: {expenses}")

# Initial list of monthly expenses
monthly_expenses: List[int] = [2200, 2350, 2600, 2130, 2190]

# Call the function with our expense data
monthly_expenses_tracker(monthly_expenses)