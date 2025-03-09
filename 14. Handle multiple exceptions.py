try:
    x=int(input("Enter Number:- "))
    print(2/x)
except ZeroDivisionError:
    print("This is ZeroDivisionError")
except ValueError:
    print("This is ValueError")
except Exception as a:
    print("Program not running because of:", a)



try:
    num = int(input("Enter a number: "))
    print(f"Square of {num} is {num ** 2}")
except ValueError:
    print("Error: Input must be a valid integer.")
else:
    print("Program executed successfully.")


