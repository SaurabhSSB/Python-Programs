"""
A module that finds the country and check if they belong to the same country or not given name of cities.
"""

# Data of the country and the name of the cities
india: list[str]= ["mumbai", "bangalore", "chennai", "delhi"]
pakistan: list[str]= ["lahore", "karachi", "islamabad"]
bangladesh: list[str]= ["dhaka", "khulna", "rangpur"]

def country(city:str )->str:
    """
    This function finds the country name given the name of the city.
    :param city: Name of a city
    :return: Name of the country that to which the city belongs to.
    """
    if city in india:
        return "india"
    elif city in pakistan:
        return "pakistan"
    elif city in bangladesh:
        return "bangladesh"
    else:
        return "not found"

def country_check(country1:str, country2:str)->bool:
    """
    This function finds if two given cities belong to the same country or not.
    :param country1: Name of first city.
    :param country2: Name of second city.
    :return: if the city belong to the same country or not.
    """
    if country1==country2:
        return True
    else:
        return False

# using try-except for handling possible value error from the user input
try:
    # Enter name of the city
    city_name1= input("Enter city name:- ")

    # Enter name of another city
    city_name2 = input("Enter city name:- ")

    # Finding the name of country with the help of country function
    country_name1= country(city_name1)

    # Finding the name of country with the help of country function
    country_name2 = country(city_name2)

    # If country name not found
    if country_name1== "not found":
        print("Name not present in the data.")

    # If country name found printing the name of the country
    else:
        print(f"{city_name1} is present in {country_name1}")

    # If country name not found
    if country_name2== "not found":
        print("Name not present in the data.")

    # If country name found printing the name of the country
    else:
        print(f"{city_name2} is present in {country_name2}")

    # Checking if the countries are available for the cities or not.
    if country_name1== 'not found' or country_name2== "not found":
        raise ValueError("Not sufficient data for finding whether the cities belong to the same country or not.")

    # Checking if the cities belong to the same country or not by using check_city function
    check_city: bool= country_check(country_name1, country_name2)

    # If the country is same.
    if check_city:
        print(f"{city_name1} and {city_name2} belong to the same {country_name1}")

    # If the countries are different.
    else:
        print(f"{city_name1} belongs to {country_name1} and {city_name2} belongs to {country_name2} thus both cities have different countries.")

except ValueError as e:
    print(f"Error: {e}")