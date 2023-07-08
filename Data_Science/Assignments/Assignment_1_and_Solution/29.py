# 29. Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.
import re

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    alphanumeric_s = re.sub(r'\W+', '', s.lower())

    # Use two pointers to check if the string is a palindrome
    left = 0
    right = len(alphanumeric_s) - 1
    while left < right:
        if alphanumeric_s[left] != alphanumeric_s[right]:
            return False
        left += 1
        right -= 1

    return True

# Get input from the user
string = input("Enter a string: ")

# Check if the string is a valid palindrome
if is_palindrome(string):
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")
