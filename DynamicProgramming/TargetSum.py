from typing import List

# Question:
# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# Logic:
# This might seem different but this is exactly the "Partition With Given Difference" problem bcos we can create two subsets such that S1 - S2 = target.

class Solution:
    def countPartitions(self, arr, d):
        n = len(arr)
        totalSum, zeros = 0, 0
        for num in arr:
            totalSum += num
            if num == 0:
                zeros += 1
        
        reqSum = (totalSum - d)
        if reqSum < 0 or reqSum%2 != 0:
            return 0
        reqSum = int(reqSum/2)
        prev = [0 for _ in range(reqSum+1)]
        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1

        if arr[0] != 0 and arr[0] <= reqSum:
            prev[arr[0]] = 1
        
        for k in range(1, n):
            curr = [0 for _ in range(reqSum+1)]
            for target in range(reqSum+1):
                not_pick = prev[target]
                pick = 0
                if arr[k] <= target:
                    pick = prev[target - arr[k]]
                curr[target] = pick + not_pick
            prev = curr
        
        return prev[reqSum]
 
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.countPartitions(nums, target)