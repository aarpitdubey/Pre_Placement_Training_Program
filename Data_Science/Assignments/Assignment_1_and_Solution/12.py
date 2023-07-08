# 12. Implement a function to check if a given string is an anagram of another string.

def is_anagram(str_a, str_b):    
    if sorted(str_a) == sorted(str_b):
        return True
    else:
        return False
    
    
if __name__ == '__main__':
    
    py_str = input("\nEnter first String here: \n").lower()
    py_str_= input("\nEnter second String here: \n").lower()
    
    if is_anagram(py_str, py_str_):
        print(f'\nThe strings : "{py_str} and {py_str_}" both are anagrams.\n')
    else:
        print(f'\nThe strings : "{py_str} and {py_str_}" are not anagrams.\n')
        