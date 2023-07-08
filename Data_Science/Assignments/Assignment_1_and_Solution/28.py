# 28. Implement a function to calculate the square root of a given number.

def square_root(number):
    if number < 0:
        raise ValueError("Square root undefined for negative numbers.")
    if number == 0:
        return 0

    x = number
    while True:
        next_x = 0.5 * (x + number / x)
        if abs(x - next_x) < 1e-10:  # Set an appropriate precision
            break
        x = next_x

    return x

# Get input from the user
number = float(input("Enter a number: "))

# Calculate the square root
sqrt = square_root(number)

# Print the square root
print("Square root:", sqrt)