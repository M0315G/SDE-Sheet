# Question:
# Given an integer n and an array of integers arr, return the Longest Increasing Subsequence which is Index-wise lexicographically smallest.
# Note - A subsequence S1 is Index-wise lexicographically smaller than a subsequence S2 if in the first position where S1 and S2 differ,
# subsequence S1 has an element that appears earlier in the array  arr than the corresponding element in S2.
# LIS  of a given sequence is defined as that longest possible subsequence all of whose elements are in increasing order. For example,
# the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and the LIS is {10, 22, 33, 50, 60, 80}


# Logic:
# We use the most optmized tabulation method and keep an additional array rem which keeps track of the last index for each sequence at index i.

class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        dp = [1]*N
        rem = [i for i in range(N)]
        maxLen = 1
        maxIdx = 0
        for idx in range(N):
            for prevIdx in range(idx):
                if arr[prevIdx] < arr[idx] and dp[prevIdx] + 1 > dp[idx]:
                        dp[idx] = dp[prevIdx] + 1
                        rem[idx] = prevIdx
            if dp[idx] > maxLen:
                maxLen = dp[idx]
                maxIdx = idx

        idx = maxIdx
        ans = [arr[idx]]
        while idx != rem[idx]:
            idx = rem[idx]
            ans.append(arr[idx])
            
        return ans[::-1]