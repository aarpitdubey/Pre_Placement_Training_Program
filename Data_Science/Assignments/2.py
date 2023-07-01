# 2. Implement a function to check if a given string is a palindrome.
# py_string="madam" is a palindrome
# py_string= "madama" is not a palindrome

# 0. Taking user inputs
py_string = input("Please enter a String here: ")

# 1. code to reverse a string
def str_reverse(py_string):
    rev_py_string = py_string[::-1].lower()
    return rev_py_string

# 2. Code to check the string is palindrome or not  
def is_palindrome():
    if py_string.lower() == str_reverse(py_string):
        print("String : {}, is palindrome".format(py_string))
    else:
        print("String : {}, is not a palindrome".format(py_string))

# 3. function calling
is_palindrome()