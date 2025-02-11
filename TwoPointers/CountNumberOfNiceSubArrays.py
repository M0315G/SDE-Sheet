from typing import List
from collections import defaultdict

# Question:
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Logic:
# Same hashMap approach.


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddMap = defaultdict(int)
        oddMap[0] += 1
        currSum = 0
        count = 0
        idx = 0
        while idx < len(nums):
            currSum += nums[idx]%2
            if oddMap[currSum-k] != 0:
                count += oddMap[currSum-k]
            oddMap[currSum] += 1
            idx += 1
        return count