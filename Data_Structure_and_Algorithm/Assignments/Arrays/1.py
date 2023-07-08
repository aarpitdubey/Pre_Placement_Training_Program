
# 💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# **Example:**
# Input: nums = [2,7,11,15], target = 9
# Output0 [0,1]

# **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][
    

def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

# Get user input for nums array
nums = input("Enter the numbers separated by spaces: ").split()
nums = [int(num) for num in nums]

# Get user input for target value
target = int(input("Enter the target value: "))

result = twoSum(nums, target)
print(result)
