# 15. Write a program to find the median of a list of numbers

# !pip install statistics
import statistics

def get_median(py_list):
    return statistics.median(py_list)

if __name__ == '__main__':
    
    py_list = input("\nEnter first List elements here: \n").split() 
    py_list = [py_list[i].lstrip('0') for i in range(0, len(py_list))]
    # Converting the list of strings numbers into a list of integers
    py_list = [eval(i) for i in py_list]
    print(f"\nOriginal list  : {(py_list)}")
    print(f"\nMedian of list : {(get_median(py_list))}\n")
