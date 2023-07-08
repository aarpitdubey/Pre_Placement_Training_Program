# 13. Write a Python program to generate all permutations of a given string.

def generate_permutation(str_u, str_p=""):
    # If string length is zero than print empty string.
    if len(str_u)==0:
        print(str_p)
        
    for i in range(len(str_u)): 
        str_s = str_p + str_u[i]
        str_r = str_u[0:i] + str_u[i+1:]
        generate_permutation(str_r, str_s)
        
if __name__ == "__main__":
    py_str = input("\nEnter a string to generate permutation\n")
    print("\nGenerating all permutations ...\n")
    generate_permutation(py_str)
    print("-"*50)