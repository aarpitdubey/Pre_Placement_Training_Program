# 22. Implement a function to find the first non-repeating character in a string.

from collections import Counter

def first_non_repeating_char(string):
    char_count = Counter(string)

    for char in string:
        if char_count[char] == 1:
            return char

    return None

input_string = input("Enter a string: ")
result = first_non_repeating_char(input_string)

if result:
    print("The first non-repeating character is:", result)
else:
    print("No non-repeating character found.")
