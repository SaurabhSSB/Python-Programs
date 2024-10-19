a= int(input("Enter first number:- "))
b= int(input("Enter Second number:- "))
c= input("Enter the Operation to be performed:- ")

match c:
    case "Addition":
        print(a+b)
    case "Subtraction":
        print(a-b)
    case "Multiplication":
        print(a*b)
    case "Division":
        print(a/b)
    case _:
        print("No Valid Operation Provided.")
