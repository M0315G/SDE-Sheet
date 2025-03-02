# Question:
# Given an array arr of non-negative integers and an integer target, the task is to count
# all subsets of the array whose sum is equal to the given target.


# Logic:
# Use the same pick or not-pick approach (refer the original problem: SubsetSum.py for all 3 variants) and if we get a sum==0 when we're out of options,
# i.e. when we've traversed the whole array we return 1

class Solution:
    def findSubsequence(self, arr, index, dp, target):
        if index < 0:
            if target == 0:
                return 1
            else:
                return 0

        if dp[index][target] != -1:
            return dp[index][target]

        not_pick = self.findSubsequence(arr, index - 1, dp, target)
        pick = 0
        if arr[index] <= target:
            pick = self.findSubsequence(arr, index - 1, dp, target - arr[index])

        dp[index][target] = pick + not_pick
        return dp[index][target]

    def perfectSum(self, arr, target):
        n = len(arr)
        dp = [[-1 for _ in range(target+1)] for _ in range(n)]
        return self.findSubsequence(arr, n-1, dp, target)