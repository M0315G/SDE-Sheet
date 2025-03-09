# Question:
# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
# A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.


# Logic:
# The idea here is to find the LCS first and then we do backtracking. The rules of backtracking are:
# 1. If str1[i] == str2[j] then we move diagonally up i.e. i-1, j-1
# 2. Else, we see where does the max value come from:
#       --> if dp[i-1][j] > dp[i][j-1] we move i -= 1 and add str1[i-1] to the answer:: because here the string str2 remains intact
#       --> else vice versa of this. 


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        elif str1 in str2:
            return str2
        elif str2 in str1:
            return str1
        
        n1, n2 = len(str1), len(str2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(n1+1):
            dp[i][0] = i
        
        for j in range(n2+1):
            dp[0][j] = j

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1

        i, j = n1, n2
        seq = []
        while i >0 and j >0:
            if str1[i-1] == str2[j-1]:
                seq.append(str1[i-1])
                i -= 1
                j -=1
            elif dp[i-1][j] < dp[i][j-1]:
                seq.append(str1[i-1])
                i -= 1 
            else:
                seq.append(str2[j-1])
                j -= 1
        
        while i > 0:
            seq.append(str1[i-1])
            i -= 1
    
        while j > 0:
            seq.append(str2[j-1])
            j -= 1

        seq = "".join(seq[::-1])
        return seq