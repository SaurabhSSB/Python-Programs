a= open("Marks.txt","r")
i=1
while True:
    x=a.readline()
    print(x)
    if not x:
        break
    y1= int(x.split(",")[0])
    y2= int(x.split(",")[1])
    y3= int(x.split(",")[2])
    y4= int(x.split(",")[3])
    y5= int(x.split(",")[4])
    print(f"Marks of Physics of Student{i}= {y1}")
    print(f"Marks of Physics of Student{i}= {y2}")
    print(f"Marks of Physics of Student{i}= {y3}")
    print(f"Marks of Physics of Student{i}= {y4}")
    print(f"Marks of Physics of Student{i}= {y5}")
    i+=1
a.close()