from collections import defaultdict
from typing import List

# Question:
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Logic:
# The idea is to store the frequency of each Sum which we can find in the array. We keep adding thigs to the current sum variable
# and then just check if currSum-k key exits in the map, if yes, increment the count by their value.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = defaultdict(int)
        sumMap[0] = 1
        n = len(nums)
        count = 0
        idx = 0
        currSum = 0
        while idx < n:
            currSum += nums[idx]
            if sumMap[currSum-k] != 0:
                count += sumMap[currSum-k]
            sumMap[currSum] += 1
            idx += 1
        return count
        

        