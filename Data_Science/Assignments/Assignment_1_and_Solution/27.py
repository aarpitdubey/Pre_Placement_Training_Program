# 27. Write a program to find the greatest common divisor (GCD) of two numbers.

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Get inputs from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the GCD
gcd = find_gcd(num1, num2)

# Print the GCD
print("GCD:", gcd)
