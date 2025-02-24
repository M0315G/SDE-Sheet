# Question:
# Given an array of positive integers arr[] and a value target, determine if there is a subset of the given array with sum equal to given target. 


# Logic:
# We use DP with memoization:
# Trick is to use the recusion of "to pick or not to pick" and keep a DP array of DP[index][tagret] telling if it's possible to achieve target at give index.

class Solution:
    def findSubset(self, arr, index, target, dp):
        if target == 0:
            return True
        if index == 0:
            return arr[index] == target
        
        if dp[index][target] != -1:
            return dp[index][target]
        
        not_take = self.findSubset(arr, index-1, target, dp)
        take = False
        if target >= arr[index]:
            take = self.findSubset(arr, index-1, target-arr[index], dp)

        dp[index][target] = take or not_take
        return dp[index][target]

    def isSubsetSum (self, arr, target):
        dp = [[-1 for _ in range(target+1)] for _ in range(len(arr)+1)]
        return self.findSubset(arr, len(arr)-1, target, dp) 