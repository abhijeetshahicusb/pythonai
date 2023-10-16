# 3. python program to find the product of a set of real no.
x=int(input("enter how many numbers of real no. you want to find the product:-"))
product=1
for i in range(x):
    real=float(input("enter a realno.-"))
    product=product*real
print("product of given sets of real no is:-",product)
