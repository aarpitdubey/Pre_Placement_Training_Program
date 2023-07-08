# 18. Implement a function to find the maximum subarray sum in a given list.

def max_subarray_sum(nums):
    if not nums:
        return 0, []

    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    subarray = []

    for i, num in enumerate(nums):
        if num > current_sum + num:
            start = i
        current_sum = max(num, current_sum + num)

        if current_sum > max_sum:
            max_sum = current_sum
            end = i
            subarray = nums[start : end + 1]

    return max_sum, subarray


# Dynamic input from the user
num_list = input("Enter a list of numbers separated by spaces: ").split()
# Convert the input string list to actual integers
nums = [int(num) for num in num_list]

result_sum, result_subarray = max_subarray_sum(nums)
print("Maximum subarray sum:", result_sum)
print("Subarray with the maximum sum:", result_subarray)