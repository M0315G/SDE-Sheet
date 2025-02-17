from typing import List

# Question:
# You are a professional robber planning to rob houses along a street. Each house has a certain amount
# of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the
# last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if
# two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
# rob tonight without alerting the police.

# Logic:
# We solve this using the approach of House Robber but this time we do it twice:
# 1. arr without last element
# 2. arr without 1st element
# then use the same approach on both of them and then get the max of it.

# The prev1 and prev2 are messed up in this but if space is not a constraint use the tabulation approach of House robber.

class Solution:
    def strategy(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        prev2, prev1 = 0, nums[-1]
        for idx in range(n-2, -1, -1):
            curr = max(prev1, prev2+nums[idx])
            prev2 = prev1
            prev1 = curr
        return prev1

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a = self.strategy(nums[:-1])
        b = self.strategy(nums[1:])
        return max(a, b)
        