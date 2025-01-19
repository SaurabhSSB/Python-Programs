"""
This module tracks the km one has run and comments on it.
"""

def check(distance_run: int) -> bool:
    """
    Asks if the user is tired and returns True if they respond with 'True', otherwise False.

    :return: Boolean indicating whether the user is tired
    """
    print(f"You have run {i+1} km")
    condition_check: str = input("Are you tired? (True/False): ").strip().lower()
    return condition_check == "true"

race_completed: bool = 1
for i in range(4):
    if check(i):
        print("You didn't finish the race")
        race_completed = 0
        break
    else:
        continue

if race_completed == 1:
    print("Congratulations! you have completed 5 km race")
else:
    print(f"You ran {i+1} km")