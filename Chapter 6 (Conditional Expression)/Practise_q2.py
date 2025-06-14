
marks1 = int(input("Enter Marks 1 : "))
marks2 = int(input("Enter Marks 2 : "))
marks3 = int(input("Enter Marks 3 : "))

# check for totawl percentage 
total_percetage = (100)*(marks1 + marks2 + marks3)/300
print(total_percetage)

if(total_percetage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed")

else :
    print("try again next year")