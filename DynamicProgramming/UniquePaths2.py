from typing import List

# Question
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries
# to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

# Logic:
# To solve with DP we have 3 ways:
# 1. Recursion with Memoization:
#   --> We traverse through every possible case and keep a 2D DP array of dp[x][y] denoting the no of ways to reach position x,y on the
#       the grid.
#       Recusive Formula:
#           f(i, j) = f(i-1, j) + f(i, j-1) (i.e. moving left and up since we're starting from end of the grid)
#               with an added condition that arr[i][j] should not be == 1

class Solution:
    def findAll(self, grid, i, j, dp):
        if i == 0 and j == 0:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        count = 0
        if i-1 > -1 and grid[i-1][j] != 1:
            count += self.findAll(grid, i-1, j, dp)
        if j-1 > -1 and grid[i][j-1] != 1:
            count += self.findAll(grid, i, j-1, dp)
        dp[i][j] = count
        return dp[i][j]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.findAll(obstacleGrid, m-1, n-1, dp)
