# 25. Write a Python program to merge two sorted lists into a single sorted list.

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Add remaining elements from list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Add remaining elements from list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


# Get inputs from the user
list1 = input("Enter elements of the first sorted list (space-separated): ").split()
list2 = input("Enter elements of the second sorted list (space-separated): ").split()

# Convert inputs to integers
list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]

# Merge the sorted lists
merged = merge_sorted_lists(list1, list2)

# Print the merged list
print("Merged list:", merged)
