from typing import List

# Question:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and
# sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Logic:
# Use the same code of Q2 with a simple change of going to idx+2 instead of idx+1 when we sell.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1, -1] for _ in range(n+1)]
        dp[n] = [0, 0]
        for idx in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(
                        -prices[idx] + dp[idx+1][0],  # Case when we buy on current day
                        dp[idx+1][1],  # Case when we didn't buy on current day
                    )
                else:
                    val = dp[idx+2][1] if idx+2 <= n else 0
                    profit = max(
                        prices[idx] + val,  # We decide to sell today
                        dp[idx+1][0],  # We didn't sell today
                    )
                dp[idx][buy] = profit

        return dp[0][1]