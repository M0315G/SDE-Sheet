# Question:
# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no
# elements without changing the order of the remaining elements.

# Logic:
# Reverse the s and treat it as LCS between those two strings.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        s2 = s[::-1]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i][j-1]
                    )
        return dp[n][n]
