# 31. Write a program to find the sum of all even numbers in a list.

def sum_even_numbers(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even

# Get inputs from the user
numbers = input("Enter a list of numbers (space-separated): ").split()

# Convert inputs to integers
numbers = [int(num) for num in numbers]

# Calculate the sum of even numbers
sum_even = sum_even_numbers(numbers)

# Print the sum of even numbers
print("Sum of even numbers:", sum_even)
