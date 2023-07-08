# 36. Implement a function to calculate the product of all elements in a list

from functools import reduce
import operator

def product_of_elements(lst):
    if not lst:
        return 0
    
    return reduce(operator.mul, lst)

input_list = [int(x) for x in input("Enter a list of numbers (space-separated): ").split()]
result = product_of_elements(input_list)
print("Product of elements:", result)
