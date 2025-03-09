try:
    a=int(input("Enter the number:- "))
    b=a/0
except ZeroDivisionError:
    print("Wrong Input")
finally:
    print("Work Done")