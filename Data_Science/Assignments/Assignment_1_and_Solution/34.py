# 34. Implement a function to find the longest common prefix among a list of strings:

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    min_len = min(len(s) for s in strs)
    i = 0
    while i < min_len:
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            i += 1
        else:
            break
    
    return strs[0][:i]

input_list = input("Enter a list of strings (comma-separated): ").split(",")
prefix = longest_common_prefix(input_list)
print("Longest common prefix:", prefix)
