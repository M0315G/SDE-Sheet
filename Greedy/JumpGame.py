from typing import List
# Question
# You are given an integer array nums. You are initially positioned at the array's first index, and each
# element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Logic:
# Iterate over all the elements and just keep a check of the maxIndex you can goto
# If the current index > maxIndex then return False
# If at end maxIndex >= n, return True, else false

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        n = len(nums) - 1
        for idx in range(n+1):
            if maxIndex < idx:
                return False
            maxIndex = max(maxIndex, idx + nums[idx])
        if maxIndex >= n:
            return True
        return False
