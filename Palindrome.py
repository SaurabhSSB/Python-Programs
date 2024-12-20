# Palindrome
a=input("Enter the String:- ")

b=0
for i in range (len(a)//2):
    if(a[i]!=a[-i-1]):
        b=1
        break

if(b==0):
    print(a, "is Palindrome.")else:
    print(a, "is not Palindrome.")
