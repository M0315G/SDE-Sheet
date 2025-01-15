from typing import List

# Question:
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Logic:
# Focus on reversal. It needs 3 reversals to get it right.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = int(k%n)
        if k == 0:
            return
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
                
