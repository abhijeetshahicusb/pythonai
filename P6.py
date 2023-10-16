#6. Python program to display the given integer in a reverse order.
x=int(input("enter the number to display reverse:-"))
rev=0
while(x>0):
    digit=x%10
    rev=rev*10+digit
    x=x//10
print("the reverse of given no. is",rev) 
