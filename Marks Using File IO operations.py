a= open("Marks.txt","r")
i=1
while True:
    x=a.readlines()
    print(x)
    if not x:
        break
    y1= x.split(",")[0]
    y2= x.split(",")[1]
    y3= x.split(",")[2]
    y4= x.split(",")[3]
    y5= x.split(",")[4]
    print(f("Marks of Physics of Student{i}= {y1}"))
    print(f("Marks of Physics of Student{i}= {y2}"))
    print(f("Marks of Physics of Student{i}= {y3}"))
    print(f("Marks of Physics of Student{i}= {y4}"))
    print(f("Marks of Physics of Student{i}= {y5}"))
    i+=1
a.close()