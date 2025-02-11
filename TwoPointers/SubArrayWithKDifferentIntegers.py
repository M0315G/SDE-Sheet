from typing import List
from collections import defaultdict

# Question:
# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

# Logic:
# I've used the nums of subarray of (<=k) - nums of subarray of (<=k-1) logic here.

class Solution:
    def find(self, nums: List[int], k):
        if k <0:
            return 0
        left, right = 0, 0
        intMap = defaultdict(int)
        count = 0
        while right < len(nums):
            intMap[nums[right]] += 1
            while len(intMap.keys()) > k:
                intMap[nums[left]] -= 1
                if intMap[nums[left]] == 0:
                    del intMap[nums[left]]
                left += 1
            count += (right - left + 1)
            right += 1
        return count
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt1 = self.find(nums, k)
        cnt2 = self.find(nums, k-1)
        # print(cnt1, cnt2)
        return cnt1 - cnt2