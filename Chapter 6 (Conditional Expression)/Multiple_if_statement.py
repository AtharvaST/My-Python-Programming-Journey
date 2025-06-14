a = int(input("Enter you Age :"))

# if Statement No : 1
if(a%2 == 0):
    print("a is even")
# End of if Statement No : 1

# if Statement No : 2
if(a>=18):
    print("you are above consent age")
    print("Good for you")

elif(a<0):
    print("you are entering invalid neagtive age.")

elif(a==0):
    print("you are entering zero age which is not valid.")
    
else:
    print("You are below consent age")
# End of if Statement No : 2

print("End of program")        
