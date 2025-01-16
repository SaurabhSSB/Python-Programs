'''
A module that helps us keep track of our favourite heroes from marvel
'''

from typing import List

def marvel_hero(heroes: List[str])-> None:
    """
    A function that helps us keep track of our favourite marvel heroes.
    :param heroes: a list that contains the name of our cherished marvel heroes
    :return: None
    """
    # Total number of heroes stored in our list
    print(f"Total number of heroes store in our list is {len(heroes)}")

    # Adding Black Panther to the end of the list
    heroes.append("Black Panther")

    # Removing Black Panther from the list
    heroes.pop()

    # Adding wolverine to the list of heroes
    heroes.append("wolverine")

    # Adding black panther at index 3
    heroes.insert(3,"black panther")

    # Removing Thor
    heroes.remove("thor")

    # Replacing hulk with dr strange
    heroes[1]= "dr Strange"

    # Sorting list heroes
    heroes.sort()

    # Print updated list of favourite heroes
    print(heroes)




heroes_marvel=['spider man','thor','hulk','iron man','captain america']
marvel_hero(heroes_marvel)