# 8. Implement a function to check if a given number is prime. 
# pip install sympy 
from sympy import isprime

def isprime_(num):
    return isprime(num)

if __name__ == '__main__':
    num = int(input("\nEnter a number: \n"))
    if isprime_(num):
        print(f"\nThe given number {num} is a prime number.\n\n")
    else:
        print(f"\nThe given number {num} is not a prime number.\n\n")