# 14. Implement a function to calculate the Fibonacci sequence up to a given number of terms.

def generate_fibonacci(nth, num_1, num_2, size):  
    if nth <= 0:
        print("\nPlease enter a positive number greator than Zero.\n")
        
    elif nth == 1:
        print(f"\nFibonacci sequence upto {nth} are:   \n")
        print(num_1)
        
    else:
        print("\nFibonacci sequence are:\n")
        
        while size < nth:
            print(num_1)
            sum_n1n2 = num_1 + num_2
            num_1 = num_2
            num_2 = sum_n1n2
            size += 1
    

if __name__ == '__main__':
    py_nth = int(input("\nEnter a number upto which you want the fibonacci sequence\n"))
    num_1, num_2 = 0, 1
    size = 0
    generate_fibonacci(py_nth, num_1, num_2, size)
    print()
    print("-"*50)