14. #14.Python program to print the numbers from a given number n till 0 using recursion
def print_numbers(n):
    if n >= 0:
        print(n)
        print_numbers(n - 1)

n = int(input("Enter a number: "))
# Call the recursive function
print_numbers(n)
