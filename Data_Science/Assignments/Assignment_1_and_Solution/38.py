# 38. Implement a function to find the missing number in a given list of consecutive numbers

def find_missing_number(lst):
    n = len(lst) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

input_list = [int(x) for x in input("Enter a list of consecutive numbers (space-separated): ").split()]
missing_number = find_missing_number(input_list)
print("Missing number:", missing_number)
