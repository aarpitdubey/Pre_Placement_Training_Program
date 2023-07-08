# 21. Write a Python program to check if two strings are anagrams of each other.

def are_anagrams(str1, str2):
    # Convert strings to lowercase and remove spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    if len(str1) != len(str2):
        return False

    char_count = [0] * 26

    for char in str1:
        char_count[ord(char) - ord('a')] += 1

    for char in str2:
        char_count[ord(char) - ord('a')] -= 1

    return all(count == 0 for count in char_count)

input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

result = are_anagrams(input_str1, input_str2)

if result:
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
