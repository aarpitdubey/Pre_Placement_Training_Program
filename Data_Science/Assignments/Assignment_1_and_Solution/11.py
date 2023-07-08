# 11. Write a program to find the common elements between two lists.

def find_common_elements(py_list, py_list_):
    set_a  = set(py_list)
    set_b  = set(py_list_) 
    
    if set_a & set_b: 
        print(f"\nThe common elements between lists are: {list(set_a & set_b)}\n")
    else:
        print(f"\n[] list, Hence no common elements found!\n") 
        
if __name__ == "__main__":
    # Enter first list elements here:
    py_list = input("\nEnter first List elements here: \n").split() 
    py_list = [py_list[i].lstrip('0') for i in range(0, len(py_list))]
    # Converting the list of strings numbers into a list of integers
    py_list = [eval(i) for i in py_list]
    
    # Enter second list elements here
    py_list_ = input("\nEnter second List elements here: \n").split() 
    py_list_ = [py_list_[i].lstrip('0') for i in range(0, len(py_list_))]
    # Converting the list of strings numbers into a list of integers
    py_list_ = [eval(i) for i in py_list_]
    find_common_elements(py_list, py_list_)
    