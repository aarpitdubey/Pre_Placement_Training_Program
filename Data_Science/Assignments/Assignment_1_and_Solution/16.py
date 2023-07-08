# 16. Implement a function to check if a given list is sorted in non-decreasing order.

def check_non_decreasing_order(smp_list):
    flag = False
    
    if smp_list == sorted(smp_list):
        flag = True
        
    if flag:
        print(f"\nList {smp_list}, IS sorted in non-decresing order\n")
    else:
        print(f"\nList {smp_list}, IS NOT sorted in non-decresing order\n")
        
        
if __name__ == "__main__":
    py_list = input("\nEnter List elements here: \n").split() 
    py_list = [py_list[i].lstrip('0') for i in range(0, len(py_list))]
    # Converting the list of strings numbers into a list of integers
    py_list = [eval(i) for i in py_list]
    check_non_decreasing_order(py_list)