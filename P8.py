#8.Python program to find the sum of the digits of an integer using a while loop
x=int(input("enter the number:-"))
summ=0
while(x>0):
    digit=x%10
    summ=summ+digit
    x=x//10
print("the sum of given no. is:-",summ)
