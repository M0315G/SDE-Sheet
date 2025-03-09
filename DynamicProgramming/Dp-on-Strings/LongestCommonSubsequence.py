# Question:
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some
# characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


# Logic:
# The base logic in DP on strings is "match" or "not-match", kinda similar to pick and not-pick of the array subsequences/
# Here if the string matches we do idx-1 for both index, else we choose the max of either of them

class Solution:
    def compare(self, text1, idx1, text2, idx2, dp):
        if idx1 < 0 or idx2 < 0:
            return 0
        
        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        
        val = 0
        if text1[idx1] == text2[idx2]:
            val = 1 + self.compare(text1, idx1-1, text2, idx2-1, dp)
        else:
            val = max(
                self.compare(text1, idx1-1, text2, idx2, dp),
                self.compare(text1, idx1, text2, idx2-1, dp)
            )
        dp[idx1][idx2] = val
        return dp[idx1][idx2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.compare(text1, n-1, text2, m-1, dp)