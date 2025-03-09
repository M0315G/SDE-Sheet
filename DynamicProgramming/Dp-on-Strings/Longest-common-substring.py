# Question:
# You are given two strings s1 and s2. Your task is to find the length of the longest common substring among the given strings.

# Logic:
# Substring is a special case of subsequence such that all the matches have to be consecutive, thus to handle it we just keep the match condition
# and discard the not-match one.

class Solution:
    def longestCommonSubstr(self, s1, s2):
        n, m = len(s1), len(s2)
        # We take n+1, m+1 matrix bcos to support the base case i.e. when
        # either i ==0 or j ==0, there is nothing to match
        # thus ideally the indexes are shifted by 1 position.
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        maxEle = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    maxEle = max(maxEle, dp[i][j])

        return maxEle