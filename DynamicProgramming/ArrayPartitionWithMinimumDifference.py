# Question:
# You are given an array 'arr' containing 'n' non-negative integers.
# Your task is to partition this array into two subsets such that the absolute difference between subset sums is minimum.
# You just need to find the minimum absolute difference considering any valid division of the array elements.

# Logic:
# This is one more variation of the DP on Subsequence problems and especially for SubsetSum:
# Here we take the total sum of all elements and then try to find if we can create a subarray with that sum
# In doing so, we'll obtain the dp array which is filled with true and false
# When looking closely we'll see that the last row the array signifies that using the whole input array nums, we can create different sums
# i.e. where dp[i] = True
# So if we consider each sum as sum for subset S1 then for S2 it will be totalSum - S1 and the diff between them will be totalSum - 2*S1

from typing import List

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    totalSum = 0
    for num in arr:
        totalSum += num
    k = totalSum//2 + 1
    prev = [False for _ in range(k+1)]
    prev[0] = True
    if arr[0] <= k:
        prev[arr[0]] = True
    for index in range(1, len(arr)):
        curr = [False]*(k+1)
        for target in range(k+1):
            not_pick = prev[target]
            pick = False
            if arr[index] <= target:
                pick = prev[target - arr[index]]
            curr[target] = pick or not_pick
        prev = curr
    # print(prev)
    minDiff = float('inf')
    for index in range(k+1):
        if prev[index]:
            minDiff = min(minDiff, abs(totalSum - index - index))
    return minDiff