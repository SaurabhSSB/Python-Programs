"""
A module that helps us counts the number of time we got head in multiple coin tosses
"""
result: list[str]= ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

def head_count()->int:
    """
    A function that will return the number of time we got head in multiple coin tosses.
    :return: the number of times head appear in an experiment.
    """
    # Declaring a variable to store the count vale
    a=0
    for i in result:
        if i=="heads":
            a+=1
    return a

# calling function to count the number of heads
print(head_count())