# 39. Write a program to find the sum of digits of a given number

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

num = int(input("Enter a number: "))
digit_sum = sum_of_digits(num)
print("Sum of digits:", digit_sum)
