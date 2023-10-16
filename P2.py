# 2. Python program to find area of a triangle whose sides are given.
a,b,c=map(int,input("enter the sides of the triangle seperated by space:").split())
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle is:",area)
