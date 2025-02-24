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

# 2. Tabulation:
#   --> We assign the initial values based on the 1st row and then keep on iterating for each row.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]



# 3. Tabulation with optimized space complexity.
#   --> Instead of using 2D array we can just keep the last row and then take the count from that.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for i in range(1, m):
            curr = [0]*n
            for j in range(n):
                curr[j] += dp[j]
                if j > 0:
                    curr[j] += curr[j-1]
            dp = curr
        return dp[-1]