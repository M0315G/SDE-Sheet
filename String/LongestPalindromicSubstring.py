# Question:
# Given a string s, return the longest palindromic substring in s.

# Logic:
# 1. We try to solve this using Dynamic Programming and to do so we consider a simple scenario:
# --> If the substring [i, j] is palindrome and if s[i-1] == s[j+1] then we can say [i-1, j+1] is also a palindrome
# --> Utilizing the same concept we construct the DP table:
#     --> first we know that each string of length 1 is a palindrome so we initialize all dp[i][i] = True
#     --> Now for even length substrings, if s[i]==s[i+1] then we can say those are palindrome too, thus dp[i][i+1] = True
#     --> Now we iterate over the remaining indices in a 2d for loop:
#         --> We've captured the values for all strings of length 1 and 2, so we start with length 3 i.e. initializing the diff from 2 to n
#         --> iterate the index i from 0 to n-diff
#         --> set j = i + diff (thus we're essentially testing if given the substring contained inside s[i:j+1] is palindrome if s[i-1:j+1+1] is a palindrome)
#         --> we check if s[i] == s[j] and dp[i+1][j-1] == True (i.e. if the current characters are same and the substring inside the current string was a palindrome)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        answer = [0, 0]
        for idx in range(n):
            dp[idx][idx] = True
        for idx in range(n-1):
            if s[idx] == s[idx+1]:
                dp[idx][idx+1] = True
                answer = [idx, idx+1]
        
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    answer = [i, j]
        a, b = answer
        return s[a:b+1]