from typing import List

# Question:
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it
# will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
# can rob tonight without alerting the police.

# Logic:
# 1. Memoization:
#   --> we recursively traverse the stack with the rule f(i) = max(f(i+1), f(i+2) + arr[i])) where f(n) denotes the maximum cash you can collect
#       if you decide to rob house n.
#       Base case: for i >=n , return 0

class Solution:
    def strategy(self, nums, idx, dp):
        if idx >= len(nums):
            return 0
        if dp[idx] != -1:
            return dp[idx]

        op1 = self.strategy(nums, idx+2, dp)
        op2 = self.strategy(nums, idx+1, dp)
        dp[idx] = max(op1 + nums[idx], op2)
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        self.strategy(nums, 0, dp)
        return dp[0]

# 2. Tabulation:
#   --> We take the bottom up approach and assign dp[0] and dp[1] = nums[-1] and num[-2] resp and then build forward with the
#       loop dp[n-i-1] = max(dp[n-i-2], dp[n-i-3] + nums[i]) while going backwards in the for loop.

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        dp[0], dp[1] = nums[-1], nums[-2]
        for idx in range(n-3, -1, -1):
            dp[n-idx-1] = max(dp[n-idx-2], dp[n-idx-3]+nums[idx])
        return dp[n-1]

# 3. Optimsed:
#   Visit the optimized approach of Count Stairs to understand this bcos the prev1 and prev2 logic here is little complex.
#   If unable to understand, write on a piece of paper and dry run.

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2, prev1 = nums[-1], nums[-2]
        for idx in range(n-3, -1, -1):
            curr = max(prev1, prev2+nums[idx])
            prev2 = prev1
            prev1 = curr
        return prev1