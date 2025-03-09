try:
    with open("Tranform.txt","r") as a:
        b= a.read()
        print(b)
except FileNotFoundError:
    print("Valhalla is waiting for you.")