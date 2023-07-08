# 41. Write a Python program to find the smallest missing positive integer in a list

def find_smallest_missing_positive(lst):
    n = len(lst)
    for i in range(n):
        while 1 <= lst[i] <= n and lst[i] != lst[lst[i] - 1]:
            lst[lst[i] - 1], lst[i] = lst[i], lst[lst[i] - 1]
    
    for i in range(n):
        if lst[i] != i + 1:
            return i + 1
    
    return n + 1

input_list = [int(x) for x in input("Enter a list of numbers (space-separated): ").split()]
missing_positive = find_smallest_missing_positive(input_list)
print("Smallest missing positive integer:", missing_positive)
