a= int(input("Enter first number:- "))
b= int(input("Enter Second number:- "))
c= input("Enter the Operation to be performed:- ")
match c:
    case "Add":
        print(a+b)
    case "Sub":
        print(a-b)
    case "Multiply":
        print(a*b)
    case "Divide":
        print(a/b)
    case _:
        print("a=",a,"b=",b)
