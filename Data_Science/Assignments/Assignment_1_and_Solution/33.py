# 33. Write a Python program to remove duplicates from a list while preserving the order.

def remove_duplicates(lst):
    unique_elements = set()
    result = []
    
    for element in lst:
        if element not in unique_elements:
            result.append(element)
            unique_elements.add(element)
    
    return result

# Get inputs from the user
lst = input("Enter a list of elements (space-separated): ").split()

# Remove duplicates while preserving order
unique_lst = remove_duplicates(lst)

# Print the list without duplicates
print("List without duplicates:", unique_lst)
