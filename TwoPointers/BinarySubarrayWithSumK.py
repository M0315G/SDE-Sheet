from typing import List
# Question:
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.

# Logic:
# One of the logic is to use the same hashmap based approach.
# A more optimized approach is to do it using the below formula:
#       (no of subarray with sum <= k) - (no of subarray with sum <= k-1)

from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sumMap = defaultdict(int)
        currSum = 0
        sumMap[currSum] = 1
        idx = 0
        count = 0
        while idx < len(nums):
            currSum += nums[idx]
            # print(currSum)
            if sumMap[currSum-goal] != 0:
                count += sumMap[currSum-goal]
            sumMap[currSum] += 1
            idx += 1
        return count