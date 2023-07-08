# Write a Python program to find the second largest number in a list

def second_largest_number(lst):
    sub_list = [i for i in lst if i < max(lst)]
    return max(sub_list)

if __name__ == '__main__':
    py_list = input("\nEnter the numerical elements: \n\n").split()
    # Removing the leading zeros in the list of string elements
    py_list = [py_list[i].lstrip('0') for i in range(0, len(py_list))]
    # Converting the list of strings numbers into a list of integers
    py_list = [eval(i) for i in py_list]
    print("\nThe second largest number in a list is: {}\n".format(second_largest_number(py_list)))