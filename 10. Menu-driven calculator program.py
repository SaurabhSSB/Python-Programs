a= int(input("Enter First number:- "))
b= int(input("Enter Second number:- "))
c= input("Choose Add, Sub, Mul, Div:- ")

match c:
    case "Add":
        print(a+b)
    case "Sub":
        print(a-b)
    case "Mul":
        print(a*b)
    case "Div":
        print(a/b)
    case _:
        print("Option not available")