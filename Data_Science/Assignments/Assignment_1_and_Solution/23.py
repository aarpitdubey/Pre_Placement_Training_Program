# 23. Write a program to find the prime factors of a given number.

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors


# Example usage
input_number = int(input("Enter a number: "))
result = prime_factors(input_number)

print("Prime factors:", result)
