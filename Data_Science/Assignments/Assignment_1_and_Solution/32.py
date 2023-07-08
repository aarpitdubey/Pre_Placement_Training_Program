# 32. Implement a function to calculate the power of a number using recursion

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif exponent % 2 == 0:
        temp = power(base, exponent // 2)
        return temp * temp
    else:
        temp = power(base, (exponent - 1) // 2)
        return base * temp * temp

# Get inputs from the user
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power
result = power(base, exponent)

# Print the result
print(f"{base} raised to the power of {exponent} is: {result}")