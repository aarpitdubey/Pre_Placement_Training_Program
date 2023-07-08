# 42. Implement a function to find the longest palindrome substring in a given string

def longest_palindrome_substring(string):
    n = len(string)
    if n < 2:
        return string
    
    start = 0
    max_len = 1
    
    def expand_around_center(left, right):
        nonlocal start, max_len
        while left >= 0 and right < n and string[left] == string[right]:
            left -= 1
            right += 1
        
        if right - left - 1 > max_len:
            start = left + 1
            max_len = right - left - 1
    
    for i in range(n):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    
    return string[start:start + max_len]

string = input("Enter a string: ")
longest_palindrome = longest_palindrome_substring(string)
print("Longest palindrome substring:", longest_palindrome)
