# Question:
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
# --> '?' Matches any single character.
# --> '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).


# Logic:
# Here we have to always check if the pattern matches the string and to do this we have multiple conditions.
# if both char are same, then it's a match else if pattern has ? then it's a match.
# Now if pattern has '*' we can treat it as 2 ways: match the current character else dont match anything.


class Solution:
    def match(self, s, i, t, j, dp):
        if j == 0:
            if i == 0:
                return True
            return False

        if i == 0:
            for r in range(1, j + 1):
                if t[r - 1] != "*":
                    return False
            return True

        if dp[i][j] != -1:
            return dp[i][j]

        ans = False
        if s[i - 1] == t[j - 1] or t[j - 1] == "?":
            ans = self.match(s, i - 1, t, j - 1, dp)

        if t[j - 1] == "*":
            ans = self.match(s, i, t, j - 1, dp) or self.match(s, i - 1, t, j, dp)
            # when '*' == ''(dont match anything)           when '*' == current character
        dp[i][j] = ans
        return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        return self.match(s, n, p, m, dp)