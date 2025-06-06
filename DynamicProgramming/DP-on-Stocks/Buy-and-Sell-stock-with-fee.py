from typing import List

# Question:
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# Note:
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.

# Logic:
# Same as Q2, just add a -fee when you sell.

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
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
                    profit = max(
                        prices[idx] + dp[idx+1][1] - fee,  # We decide to sell today
                        dp[idx+1][0],  # We didn't sell today
                    )
                dp[idx][buy] = profit

        return dp[0][1]