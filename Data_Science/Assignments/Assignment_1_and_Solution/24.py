# 24. Implement a function to check if a given number is a power of two.

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

input_number = int(input("Enter a number: "))
result = is_power_of_two(input_number)

if result:
    print("The number is a power of two.")
else:
    print("The number is not a power of two.")
