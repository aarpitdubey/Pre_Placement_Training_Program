# 17. Write a Python program to find the intersection of two lists.

def intersection(list_a, list_b):
    return sorted(list(set(list_a) & set(list_b)))

if __name__ == '__main__':
    py_list = input("\nEnter first List elements here: \n").split() 
    py_list = [py_list[i].lstrip('0') for i in range(0, len(py_list))]
    # Converting the list of strings numbers into a list of integers
    py_list = [eval(i) for i in py_list]
    py_list_ = input("\nEnter second List elements here: \n").split() 
    py_list_ = [py_list_[i].lstrip('0') for i in range(0, len(py_list_))]
    # Converting the list of strings numbers into a list of integers
    py_list_ = [eval(i) for i in py_list_]
    
    print(f"\nIntersection of the two list:\n{intersection(py_list, py_list_)}\n")