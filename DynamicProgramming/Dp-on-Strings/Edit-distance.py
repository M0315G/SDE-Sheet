# Question:
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# -> Insert a character
# -> Delete a character
# -> Replace a character

# Logic:
# The idea here is to take the match and not-match approach and when the characters don't match we explore the 3 operations we have.
# 1. for insertion, we insert the character at i+1 th position.
# 2. for deletion, we delete the current character at i th position.
# 3. For replace, we replace the ith char with jth char.



class Solution:
    def count(self, s, i, t, j, dp):
        if j == 0:
            return i # We dont return i+1 bcos i is 1-indexed
        if i == 0:
            return j # We dont return j+1 bcos j is 1-indexed
        
        if dp[i][j] != -1:
            return dp[i][j]
    
        ans = -1
        if s[i-1] == t[j-1]:
            ans = self.count(s, i-1, t, j-1, dp)
        else:
            ans = min(
                self.count(s, i-1, t, j, dp), # Delete operation i.e. deleted ith char from s.  
                self.count(s, i-1, t, j-1, dp), # Replace operation i.e. repalaced ith char of s with jth char of t.
                self.count(s, i, t, j-1, dp), # Insert operation i.e. inserted jth char of t at (i+1)th position.
            ) + 1 # This one is for performing any 1 of the above operation.
        
        dp[i][j] = ans
        return dp[i][j]


    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1) ]
        return self.count(word1, n, word2, m, dp)