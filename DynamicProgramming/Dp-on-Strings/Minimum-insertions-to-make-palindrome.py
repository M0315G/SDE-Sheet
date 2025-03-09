# Question:
# Given a string s. In one step you can insert any character at any index of the string.
# Return the minimum number of steps to make s palindrome.
# A Palindrome String is one that reads the same backward as well as forward.

# logic:
# We use DP to find the maximum longest palindromic sequence and then the answer is just n - max_len.

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        prev = [0 for _ in range(n+1)]

        s2 = s[::-1]
        for i in range(1, n+1):
            curr = [0 for _ in range(n+1)]
            for j in range(1, n+1):
                if s[i-1] == s2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        # print(prev)
        return n - prev[-1]