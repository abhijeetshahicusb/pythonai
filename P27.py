#27. Python program to find the Nth term in a Fibonacci series using recursion. 
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Input the value of N
N = int(input("Enter the value of N: "))

if N < 0:
    print("Invalid input. Please enter a non-negative integer.")
else:
    result = fibonacci_recursive(N)
    print(f"The {N}-th term in the Fibonacci series is: {result}")
