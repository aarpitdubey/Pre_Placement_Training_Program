# 44. Implement a function to check if a given number is a perfect number

def is_perfect_number(num):
    if num <= 0:
        return False

    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

num = int(input("Enter a number: "))
if is_perfect_number(num):
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")
