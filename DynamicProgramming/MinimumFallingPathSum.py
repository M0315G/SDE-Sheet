from typing import List

# Question:
# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below
# or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1),
# (row + 1, col), or (row + 1, col + 1).


# Logic:
# We use DP to solve this:
# 1. Use Recursion with memoization:
#      --> We traverse the whole matrix and use the recursion function: f(i, j) = min(f(i+1, j-1), f(i+1, j), f(i+1, j+1)) + arr[i][j]
#       with the base case of if row == n, return.

class Solution:
    def calculateSum(self, matrix, row, col, dp):
        if row == len(matrix) - 1:
            dp[row][col] = matrix[row][col]
            return dp[row][col]

        if dp[row][col] != float('inf'):
            return dp[row][col]
        
        summation = self.calculateSum(matrix, row+1, col, dp)
        if col > 0:
            summation = min(summation, self.calculateSum(matrix, row+1, col-1, dp))
        if col + 1 < len(matrix):
            summation = min(summation, self.calculateSum(matrix, row+1, col+1, dp))
        dp[row][col] = matrix[row][col] + summation
        return dp[row][col]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for col in range(n):
            self.calculateSum(matrix, 0, col, dp)
        return min(dp[0])