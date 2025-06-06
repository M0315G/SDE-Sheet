from typing import List

# Question:
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

# Logic:
# We consider the same pick/not-pick solution but this time we condition on an action: buy i.e. if we've bought the stock previously
# Thus if we've bought the stock, we have 2 choices either sell the stock or not.
# And if we haven't bought, we can either buy or not-buy.

# Recursion: Memoization

class Solution:
    def choose(self, prices, idx, buy, dp):
        if idx == len(prices):
            return 0
        
        if dp[idx][buy] != -1:
            return dp[idx][buy]
        
        profit = 0
        if buy:
            profit = max(
                -prices[idx] + self.choose(prices, idx+1, 0, dp),  # Case when we buy on current day
                self.choose(prices, idx+1, 1, dp),  # Case when we didn't buy on current day
            )
        else:
            profit = max(
                prices[idx] + self.choose(prices, idx+1, 1, dp),  # We decide to sell today
                self.choose(prices, idx+1, 0, dp),  # We didn't sell today
            )
        
        dp[idx][buy] = profit
        return dp[idx][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1, -1] for _ in range(n)]
        return self.choose(prices, 0, 1, dp)


# Tabulation

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1, -1] for _ in range(n+1)]
        
        dp[n] = [0, 0]
        buy = 0
        for idx in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(
                        -prices[idx] + dp[idx+1][0],  # Case when we buy on current day
                        dp[idx+1][1],  # Case when we didn't buy on current day
                    )
                else:
                    profit = max(
                        prices[idx] + dp[idx+1][1],  # We decide to sell today
                        dp[idx+1][0],  # We didn't sell today
                    )
                dp[idx][buy] = profit

        return dp[0][1]


# Space optimized
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0, 0]
        for idx in range(n-1, -1, -1):
            curr = [-1, -1]
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(
                        -prices[idx] + dp[0],  # Case when we buy on current day
                        dp[1],  # Case when we didn't buy on current day
                    )
                else:
                    profit = max(
                        prices[idx] + dp[1],  # We decide to sell today
                        dp[0],  # We didn't sell today
                    )
                curr[buy] = profit
            dp = curr

        return dp[1]