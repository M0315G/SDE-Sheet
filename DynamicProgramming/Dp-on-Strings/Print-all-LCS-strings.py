# Question:
# You are given two strings s and t. Now your task is to print all longest common sub-sequences in lexicographical order.
# Note -  A Sub-sequence is derived from another string by deleting some or none of the elements without changing the order of the remaining elements.


# Logic:
# This is an extension of the LCS problem where we have to print all the LCS.
# To do this we backtrack on the DP array, if only 1 LCS asked (i.e print any LCS) then we only need to do this in a simple while loop
# but in this question we're asked to get all LCS, thus we need a function.
# Core logic is:
#   When i == j, we move i-1, j-1
#   Else we check if dp[i-1][j] == dp[i][j], then we travese that
#           Also check of dp[i][j-1] == dp[i][j]
#   This gives all the possible string combinations
# Lastly, keep a visited set.

class Solution:
    def compare(self, text1, idx1, text2, idx2, dp):
        if idx1 == 0 or idx2 == 0:
            return 0
        
        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        
        val = 0
        if text1[idx1-1] == text2[idx2-1]:
            val = 1 + self.compare(text1, idx1-1, text2, idx2-1, dp)
        else:
            val = max(
                self.compare(text1, idx1-1, text2, idx2, dp),
                self.compare(text1, idx1, text2, idx2-1, dp)
            )
        dp[idx1][idx2] = val
        return dp[idx1][idx2]
    
    def all_longest_common_subsequences(self, s, t):
        n, m = len(s), len(t)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        self.compare(s, n, t, m, dp)

        ans = []
        visited = set()
        
        def func(i, j, txt):
            if i == 0 or j == 0:
                ans.append(txt)
                return
        
            if (i, j, txt) in visited:
                return
        
            visited.add((i, j, txt))
        
            if s[i-1] == t[j-1]:
                func(i-1, j-1, txt + s[i-1])
            else:
                if dp[i][j] == dp[i-1][j]:
                    func(i-1, j, txt)
                if dp[i][j] == dp[i][j-1]:
                    func(i, j-1, txt)
            

        func(n, m, "")
        return ans