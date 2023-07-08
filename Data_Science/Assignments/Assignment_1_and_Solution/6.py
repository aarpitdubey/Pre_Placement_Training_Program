# 6. Implement a function to remove duplicate elements from a list. 

def remove_duplicate(lst):
    py_set = set(lst)
    py_list = list(py_set)
    return py_list

if __name__ == "__main__":
    py_list = input("\nEnter the numerical elements: \n\n").split()
    # Removing the leading zeros in the list of string elements
    py_list = [py_list[i].lstrip('0') for i in range(0, len(py_list))]
    # Converting the list of strings numbers into a list of integers
    py_list = [eval(i) for i in py_list]
    py_list = remove_duplicate(py_list)
    print("\n\n-: After removal of duplicates :- \n{}\n\n".format(py_list))