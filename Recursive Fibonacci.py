def fibonacci(a):
    if(a==0):
        return(0)
    if (a==1):
        return(1)
    return(fibonacci(a-1)+fibonacci(a-2))

x= int(input("Enter number:- "))
n=fibonacci(x)
print(n)