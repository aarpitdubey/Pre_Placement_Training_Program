# 9. Write a Python program to sort a list of integers in ascending order.

def sort_list(py_list):
    return sorted(py_list)

if __name__ == '__main__':
    # Taking the input (string) and converting them into a list using split( )
    py_list = input("\nEnter List elements here: \n").split() 
    py_list = [py_list[i].lstrip('0') for i in range(0, len(py_list))]
    # Converting the list of strings numbers into a list of integers
    py_list = [eval(i) for i in py_list]
    print(f"\nThe sorted list are : \n{sort_list(py_list)}\n")