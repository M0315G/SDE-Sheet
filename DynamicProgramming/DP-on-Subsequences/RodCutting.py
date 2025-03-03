# Question:
# Given a rod of length n(size of price) inches and an array of prices, price.
# price[i] denotes the value of a piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.


# Logic:
# We have to determine the best way to cut the rod into pieces such as to maximize the profit, thus we use the algorithm used in Coin Change.py
# since multiple pieces of same length can be used.

class Solution:
    def cut(self, price, index, n, dp):
        if n == 0:
            return 0
        if index == 1:
            return (n//index)*price[index-1]

        if dp[index-1][n] != -1:
            return dp[index-1][n]
        
        not_pick = self.cut(price, index-1, n, dp)
        pick = 0
        if n - index >= 0:
            pick = self.cut(price, index, n - index, dp) + price[index-1]
        
        dp[index-1][n] = max(pick, not_pick)
        return dp[index-1][n]

    def cutRod(self, price):
        n = len(price)
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        return self.cut(price, n, n, dp)