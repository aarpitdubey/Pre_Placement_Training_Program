# 7. Write a program to calculate the factorial of a given number. 
import math as m

def fact(num):
    return m.factorial(num)

if __name__ == '__main__':
    py_num = int(input("\nEnter your number here: \n"))
    print("\nThe factorial of {} is : {}\n\n6".format(py_num, fact(py_num)))
    