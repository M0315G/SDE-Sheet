from typing import List

# Question:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


# Logic:
# Since here max transactions can be only 2 (instead of infinite in Q2), we introduce additional dimension of capacity
# in the dp array.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1, -1, -1] for _ in range(2)] for _ in range(n+1)]
        
        # For the base case where capacity == 0
        for i in range(n+1):
            for buy in range(2):
                dp[i][buy][0] = 0
            
        # For the base case where idx == n
        for buy in range(2):
            for cap in range(3):
                dp[n][buy][cap] = 0

        buy = 0
        for idx in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    profit = 0
                    if buy:
                        profit = max(
                            -prices[idx] + dp[idx+1][0][cap],  # Case when we buy on current day
                            dp[idx+1][1][cap],  # Case when we didn't buy on current day
                        )
                    else:
                        profit = max(
                            prices[idx] + dp[idx+1][1][cap-1],  # We decide to sell today
                            dp[idx+1][0][cap],  # We didn't sell today
                        )
                    dp[idx][buy][cap] = profit

        return dp[0][1][2]