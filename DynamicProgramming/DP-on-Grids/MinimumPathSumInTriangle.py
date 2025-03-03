from typing import List

# Question:
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on
# index i on the current row, you may move to either index i or index i + 1 on the next row.

# Logic:
# We use DP to solve this:
# 1. Use Recursion with memoization:
#      --> We traverse the whole matrix and use the recursion function: f(i, j) = min(f(i+1, j), f(i+1, j+1)
#       The only catch is to manage the row and col since it's a triangle.

class Solution:
    def findMinimum(self, triangle, row, col, dp):
        if row == len(triangle)-1:
            return triangle[row][col]

        if dp[row][col] != -1:
            return dp[row][col]

        left = self.findMinimum(triangle, row+1, col, dp)
        right = self.findMinimum(triangle, row+1, col+1, dp)
        dp[row][col] = min(left, right) + triangle[row][col]
        return dp[row][col]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[-1 for _ in range(len(triangle[i]))] for i in range(m)]
        return self.findMinimum(triangle, 0, 0, dp)

# 2. With Tabulation
# We go the bottom up approach which will be to start from n-1 and go towards 0

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[-1 for j in range(len(triangle[i]))] for i in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(i, -1, -1):
                if i == m-1:
                    dp[i][j] = triangle[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]

# 3. Space optimization
# We can optimize the space of the DP array to only keep the last row, by that way we can reduce the space in the tabulation method.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        prev = [triangle[-1][j] for j in range(len(triangle[-1]))]
        for i in range(m-2, -1, -1):
            curr = [-1]*(i+1)
            for j in range(i, -1, -1):
                curr[j] = min(prev[j], prev[j+1]) + triangle[i][j]
            prev = curr
        return prev[0]