#16. Python program to display the sum of n numbers using a list.
n = int(input("Enter the number of values: "))

# Initialize an empty list to store the values
values = []

# Input the values and add them to the list
for i in range(n):
    value = float(input(f"Enter value {i + 1}: "))
    values.append(value)

# Calculate the sum of the values using the sum() function
total_sum = sum(values)
print(f"The sum of the {n} values is {total_sum}")
