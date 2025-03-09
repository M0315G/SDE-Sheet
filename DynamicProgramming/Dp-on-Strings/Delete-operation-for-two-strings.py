# Question:
# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
# In one step, you can delete exactly one character in either string.

# Logic:
# The logic is simple, take the longest common subsequence from both strings and everything else needs to be deleted so answer will be
# n1 - max_len + n2 - max_len

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(
                        dp[i][j-1],
                        dp[i-1][j],
                    )
        
        return n1 - dp[n1][n2] + n2 - dp[n1][n2]