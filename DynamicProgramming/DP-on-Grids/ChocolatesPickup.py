# Question:
# You are given an n rows and m cols matrix grid representing a field of chocolates where grid[i][j] represents the number of
# chocolates that you can collect from the (i, j) cell.
# You have two robots that can collect chocolates for you:

# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of chocolates collection using both robots by following the rules below:

# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all chocolates, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the chocolates.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.

# Logic:
# We use DP to perform memoization and traverse the path of both robots simulateously in recursion

class Solution:
    def pickChocolate(self, grid, i, j1, j2, dp, m, n):
        if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
            return float('-inf')
        if i == n-1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]
        
        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]
        
        maxChocolates = 0
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if j1 == j2:
                    maxChocolates = max(
                        maxChocolates,
                        grid[i][j1] + self.pickChocolate(grid, i+1, j1+a, j2+b, dp, m, n)
                    )
                else:
                    maxChocolates = max(
                        maxChocolates,
                        grid[i][j1] + grid[i][j2] + self.pickChocolate(grid, i+1, j1+a, j2+b, dp, m, n)
                    )
        dp[i][j1][j2] = maxChocolates
        return dp[i][j1][j2]

    def solve(self, n, m, grid):
        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        return self.pickChocolate(grid, 0, 0, m-1, dp, m, n)