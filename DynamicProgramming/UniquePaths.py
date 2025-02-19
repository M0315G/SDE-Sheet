# Question:
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries
# to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 10^9

# Logic:
# To solve with DP we have 3 ways:
# 1. Recursion with Memoization:
#   --> We traverse through every possible case and keep a 2D DP array of dp[x][y] denoting the no of ways to reach position x,y on the
#       the grid.
#       Recusive Formula:
#           f(i, j) = f(i-1, j) + f(i, j-1) (i.e. moving left and up since we're starting from end of the grid)

class Solution:
    def findAll(self, m, n, i, j, dp):
        if i == 0 and j == 0:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        count = 0
        if i-1 > -1:
            count += self.findAll(m, n, i-1, j, dp)
        if j-1 > -1:
            count += self.findAll(m, n, i, j-1, dp)
        dp[i][j] = count
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.findAll(m, n, m-1, n-1, dp)

