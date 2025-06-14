
n = int(input("Enter a number :"))

for i in range(2,n):
    if(n%i) == 0 :
        print("your number is not prime number")
        break
else :
    print("Yoor number is prime number.")