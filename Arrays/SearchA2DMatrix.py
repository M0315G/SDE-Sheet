from typing import List

# Question:
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# Logic:
# A brute force approach will be to run the loop O(n^2) times and just search for the target.
# Next, the optimised solution will be to run the loop for each row and then apply a binary search in each row to search for the target.
# Next, the most optimised solution would be if you binary search across the 2D matrix --> image it to be a 1D sorted array and apply binary search
#   --> when you get your mid point, just translate that to the respective row and col index using the /n and %n rule to check where the target lies.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, (m*n - 1)
        while (low <= high):
            mid = int((low+high)/2)
            row = int(mid/n)
            col = mid%n
            # print(row, col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid+1
            else:
                high = mid-1
        return False