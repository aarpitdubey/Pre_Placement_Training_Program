# 45. Write a Python program to remove all duplicates from a string

def remove_duplicates(string):
    unique_chars = set(string)
    return ''.join(unique_chars)

string = input("Enter a string: ")
result = remove_duplicates(string)
print("String with duplicates removed:", result)
