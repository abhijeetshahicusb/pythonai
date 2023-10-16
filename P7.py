#7.Python program to find the geometric mean of n numbers.
count=0
product=1.0
n=int(input("enter the number of mumbers to find G.M"))
while(count<n):
    num=float(input("enter the number:-"))
    count=count+1
    product=product*num
    geometric_mean=pow(product,1.0/n)
print("the geometric mean is:",geometric_mean)
