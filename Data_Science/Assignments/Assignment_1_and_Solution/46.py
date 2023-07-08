# 46. Implement a function to find the first missing positive

def find_first_missing_positive(nums):
    n = len(nums)

    # Move positive numbers to their correct positions
    for i in range(n):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Find the first missing positive number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

nums = [int(x) for x in input("Enter a list of numbers (space-separated): ").split()]
missing_positive = find_first_missing_positive(nums)
print("First missing positive integer:", missing_positive)
