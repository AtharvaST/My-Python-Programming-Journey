n1 = int(input("enter Number 1 : "))
n2 = int(input("enter Number 2 : "))
n3 = int(input("enter Number 3 : "))
n4 = int(input("enter Number 4 : "))

if(n1>n2 and n1>n3 and n1>n4):
    print("Gretest number is n1 : " , n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("Gretest number is n2 : " , n2)
elif(n3>n2 and n3>n4 and n3>n1):
    print("Gretest number is n3 : " , n3)
elif(n4>n2 and n4>n3 and n4>n1):
    print("Gretest number is n4 : " , n4)