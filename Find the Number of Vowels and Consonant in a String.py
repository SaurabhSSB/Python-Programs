a= input(" Enter the String:- ")
b=len(a)
v=0
c=0

for i in range(0,b):
    if(a[i]== "a" or a[i]== "e" or a[i]== "i" or a[i]== "o" or a[i]== "u" or a[i]== "A" or a[i]== "E" or a[i]== "I" or a[i]== "O" or a[i]== "U"):
        v+=1
    else:
        c+=1

print("There are ",v,"Vowels and there are ",c,"Consonants")