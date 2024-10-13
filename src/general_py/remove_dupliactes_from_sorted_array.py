"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

"""
Time complexity: O(n)
Space complexity: O(1)
make e sure the array is not empty
initialize i to 0 the first element of the array
iterate through the array starting from the second element comparing it to the first element
if the element are not equal, increment i, it is now pointing to the next unique element
repeat the process until the end of the array.

"""
