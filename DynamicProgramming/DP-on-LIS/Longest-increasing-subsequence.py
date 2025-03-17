from typing import List

# Question:
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Logic:
# We use the basic pick or not pick logic modified to make sure all elements are in increasing order.

class Solution:
    def solve(self, nums, idx, prevIdx, dp):
        if idx == len(nums):
            return 0

        if dp[idx][prevIdx+1] != -1:
            return dp[idx][prevIdx+1]
    
        maxLen = 0
        maxLen = max(maxLen, self.solve(nums, idx+1, prevIdx, dp))
        if prevIdx == -1 or nums[idx] > nums[prevIdx]:
            maxLen = max(maxLen, self.solve(nums, idx+1, idx, dp) + 1)

        dp[idx][prevIdx+1] = maxLen
        return dp[idx][prevIdx+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        return self.solve(nums, 0, -1, dp)
    

# Tabulated and space optimized:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        prev, curr = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
        
        for idx in range(n-1, -1, -1):
            for prevIdx in range(idx-1, -2, -1):
                maxLen = prev[prevIdx+1]
                if prevIdx == -1 or nums[idx] > nums[prevIdx]:
                    maxLen = max(maxLen, prev[idx+1] + 1)
                curr[prevIdx+1] = maxLen
            prev = curr

        return prev[-1+1]


# Tabulation with optmized more for storage : only O(n) storage

def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        maxLen = 1
        for idx in range(n):
            for prevIdx in range(idx):
                if nums[prevIdx] < nums[idx]:
                    dp[idx] = max( dp[prevIdx] + 1, dp[idx] )
            maxLen = max(maxLen, dp[idx])
        return maxLen