# 26. Implement a function to find the mode of a list of numbers.

from collections import Counter

def find_mode(numbers):
    counter = Counter(numbers)
    max_count = max(counter.values())
    mode = [num for num, count in counter.items() if count == max_count]
    return mode

# Get inputs from the user
numbers = input("Enter a list of numbers (space-separated): ").split()

# Convert inputs to integers
numbers = [int(num) for num in numbers]

# Find the mode
mode = find_mode(numbers)

# Print the mode
print("Mode:", mode)
