from typing import List
# Question:
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# Logic:
# We use DP to solve this:
# 1. Use Recursion with memoization:
#      --> We traverse the whole matrix and use the recursion function: f(i, j) = min(f(i-1, j), f[i, j-1])

class Solution:
    def findMinimum(self, grid, i, j, dp):
        if i == 0 and j == 0:
            return grid[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        minVal = float('inf')
        if i-1 > -1:
            minVal = min(minVal, self.findMinimum(grid, i-1, j, dp))
        if j-1 > -1:
            minVal = min(minVal, self.findMinimum(grid, i, j-1, dp))
        dp[i][j] = minVal + grid[i][j]
        return dp[i][j]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.findMinimum(grid, m-1, n-1, dp)