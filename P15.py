#15. Python program to find the factorial of a number using recursion

def recur_fact(n):
    if n==1:
        return n
    else:
        return n*recur_fact(n-1)
n=int(input("enter the no to finf factorial"))
print("the factorial of",n,"is",recur_fact(n))
