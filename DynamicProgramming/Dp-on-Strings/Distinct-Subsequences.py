# Question:
# Given two strings s and t, return the number of distinct subsequences of s which equals t.
# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Logic:
# This uses the classis match and not-match paradigm of DP with just a simple variation that if it matches we compare for both cases:
# 1. this is the only match
# 2. there are other matches too 

class Solution:
    def count(self, s, i, t, j, dp):
        if j == 0:
            return 1
        if i == 0:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
    
        ans = -1
        if s[i-1] == t[j-1]:
            ans = self.count(s, i-1, t, j-1, dp) + self.count(s, i-1, t, j, dp)
        else:
            ans = self.count(s, i-1, t, j, dp)
        
        dp[i][j] = ans
        return dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        return self.count(s, n, t, m, dp)