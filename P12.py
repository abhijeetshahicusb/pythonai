#12. Python program to generate the prime numbers from 1 to N.
num=int(input("enter the number upto which you want to generate prime no."))
for n in range(2,num):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)