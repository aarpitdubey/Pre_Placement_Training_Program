# 19. Write a program to remove all vowels from a given string.

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string if char not in vowels)

input_string = input("Enter a string: ")
result = remove_vowels(input_string)
print("String after removing vowels:", result)