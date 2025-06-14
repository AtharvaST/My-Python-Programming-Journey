a = int(input("Enter you Age :"))

#if elif else ladder
if(a>=18):
    print("you are above consent age")
    print("Good for you")

elif(a<0):
    print("you are entering invalid neagtive age.")

elif(a==0):
    print("you are entering zero age which is not valid.")
    
else:
    print("You are below consent age")

print("End of program")        
