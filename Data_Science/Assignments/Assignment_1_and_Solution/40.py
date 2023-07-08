# 40. Implement a function to check if a given string is a valid palindrome considering case sensitivity

def is_palindrome(string):
    return string == string[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")
