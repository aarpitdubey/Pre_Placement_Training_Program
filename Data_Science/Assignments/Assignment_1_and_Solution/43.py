# 43. Write a program to find the number of occurrences of a given element in a list

def count_occurrences(lst, element):
    return lst.count(element)

input_list = [int(x) for x in input("Enter a list of numbers (space-separated): ").split()]
target_element = int(input("Enter the element to count occurrences: "))
occurrences = count_occurrences(input_list, target_element)
print("Number of occurrences:", occurrences)
