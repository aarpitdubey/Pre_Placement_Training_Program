# 35. Write a program to check if a given number is a perfect square

def is_perfect_square(num):
    if num < 0:
        return False
    
    root = int(num ** 0.5)
    return root * root == num

num = int(input("Enter a number: "))
if is_perfect_square(num):
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")
