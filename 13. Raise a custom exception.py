class Cstm(Exception):
    pass






try:
    a=int(input("Enter 2:- "))
    if(a==2):
        raise Cstm("You Entered 2!")
    else:
        print("Smart Choice")
except Cstm:
    print("Custom Exception")



class NegativeNumberError(Exception):
    pass

num = -1
if num < 0:
    raise NegativeNumberError("Negative number not allowed.")
