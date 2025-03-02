from typing import List

# Question:
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements
# in both subsets is equal or false otherwise.

# Logic:
# We can frame this question in form of the "Subset Sum" problem i.e. instead of checking if we can find 2 subsets with equal sum we try and find
# a single subset with sum = total/2.
# If total is odd, we return false.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0
        for idx in nums:
            totalSum += idx
        if totalSum % 2 != 0:
            return False
        else:
            target = totalSum//2
            n = len(nums)
            dp = [[False for _ in range(target+1)] for _ in range(n)]
            for i in range(n):
                dp[i][0] = True
            # dp[0][target] = True
            for i in range(1, n):
                for j in range(1, target+1):
                    not_take = dp[i-1][j]
                    take = False
                    if target >= nums[i]:
                        take = dp[i-1][j-nums[i]]
                    dp[i][j] = take or not_take
            # print(dp)
            return dp[n-1][target]
        