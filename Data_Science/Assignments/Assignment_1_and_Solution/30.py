# 30. Implement a function to find the minimum element in a rotated sorted list.

def find_minimum(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# Get inputs from the user
nums = input("Enter a rotated sorted list of numbers (space-separated): ").split()

# Convert inputs to integers
nums = [int(num) for num in nums]

# Find the minimum element
minimum = find_minimum(nums)

# Print the minimum element
print("Minimum element:", minimum)
