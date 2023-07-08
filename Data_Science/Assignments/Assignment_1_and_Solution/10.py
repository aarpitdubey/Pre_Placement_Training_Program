# 10. Implement a function to find the sum of all numbers in a list.

def sum_all(py_list):
    return sum(py_list)

if __name__ == '__main__':
    py_list = input("\nEnter List elements here: \n").split() 
    py_list = [py_list[i].lstrip('0') for i in range(0, len(py_list))]
    # Converting the list of strings numbers into a list of integers
    py_list = [eval(i) for i in py_list]
    print(f" \nSum of all the element in List is : {sum_all(py_list)}\n")