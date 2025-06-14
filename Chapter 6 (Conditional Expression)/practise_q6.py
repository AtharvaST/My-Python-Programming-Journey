
mark = int(input("Enter your marks : "))

if(mark<=100 and mark >= 90):
    print("your grade is : Ex" , mark)
elif(mark<=90 and mark >= 80):
    print("your grade is : A" , mark)

elif(mark<=80 and mark >= 70):
    print("your grade is : B" , mark)

elif(mark<=70 and mark >= 60):
    print("your grade is : C" , mark)

elif(mark<=60 and mark >= 50):
    print("your grade is : D" , mark)

elif(mark<50):
    print("your grade is : F  " , mark)