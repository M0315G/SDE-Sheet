from typing import List

# Question:
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Logic:
# Brute force solution would be to start from the last index and whenever you encounter a zero, we shift all elements to the left.
# A better solution would be to think of this as tranferring all the non-negative elements in the front and thus we do that by maintaining a pointer.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        n = len(nums)
        for i in range(n):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        

                

        