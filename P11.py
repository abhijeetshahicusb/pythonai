#11. Python program to check whether the given integer is a prime number or not.
n=int(input("enter the number:-"))
if n==1:
    print(n,"is not a prime no.")
elif n>1:
    for i in range(2,n):
        if(n%i)==0:
            print(n,"is not a prime no.")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is not a prime number")
            
            
