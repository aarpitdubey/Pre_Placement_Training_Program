# 💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# - Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# - Return k.

# **Example :**
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_*,_*]

# **Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)[

def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# Get user input for nums array
nums = input("Enter the numbers separated by spaces: ").split()
nums = [int(num) for num in nums]

# Get user input for val
val = int(input("Enter the value to remove: "))

k = removeElement(nums, val)
print("k =", k)
print("nums =", nums[:k], end="")
print("_* " * (len(nums) - k))