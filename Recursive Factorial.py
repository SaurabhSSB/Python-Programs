def factorial(a):
    if(a==1 or a==0):

        return(1)
    return(a*factorial(a-1))
x=int(input("Enter Number:- "))
n=factorial(x)
print(n)