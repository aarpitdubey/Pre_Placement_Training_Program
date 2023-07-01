# 3. Write a program to find the largest element in a given list.
# py_list = 00002 00000004 06 21

# Taking the input (string) and converting them into a list using split( )
py_list = input("enter the number of numerical elements here: \n\n").split() # give py_list = ["2", "3", "4", "21"]

# Removing the leading zeros in the list of string elements
py_list = [py_list[i].lstrip('0') for i in range(0, len(py_list))]

# Converting the list of strings numbers into a list of integers
py_list = [eval(i) for i in py_list]

# Using the max() function  to find th largest number
max_elements = max(py_list)


print("\nThe Largest number in this list is : {}\n".format(max_elements))