from typing import List

# Question:
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Logic:
# Similat to Q3, just the capacity is dynamic here instead of just 2.

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]
        
        # For the base case where capacity == 0
        for i in range(n+1):
            for buy in range(2):
                dp[i][buy][0] = 0
            
        # For the base case where idx == n
        for buy in range(2):
            for cap in range(k+1):
                dp[n][buy][cap] = 0

        buy = 0
        for idx in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, k+1):
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

        return dp[0][1][k]


# Solution 2:
# A very good space optmized solution is instead of taking 3D array we can do the same with 2D array if we consider the no of transactions i.e.
# For k transactions i can buy 1 time and sell 1 time each so total transactions become 2*k so we can keep this as the 2nd dimension.

# A simple recursive solution to it is:

class Solution:
    def choose(self, prices, idx, tranNo, dp):
        if idx == len(prices) or tranNo == 4:
            return 0
        
        if dp[idx][tranNo] != -1:
            return dp[idx][tranNo]
        
        profit = 0
        if tranNo % 2 == 0: # this means time to buy
            profit = max(
                -prices[idx] + self.choose(prices, idx+1, tranNo+1, dp),  # Case when we buy on current day so tranNo increases
                self.choose(prices, idx+1, tranNo, dp),  # Case when we didn't buy on current day so tranNo remains same
            )
        else:
            profit = max(
                prices[idx] + self.choose(prices, idx+1, tranNo+1, dp),  # We decide to sell today
                self.choose(prices, idx+1, tranNo, dp),  # We didn't sell today
            )
        
        dp[idx][tranNo] = profit
        return dp[idx][tranNo]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        transactions = 2*k  # Considering 1 Buy and 1 Sell for each transaction
        dp = [[-1 for _ in range(transactions)] for _ in range(n)]
        return self.choose(prices, 0, 0, dp)


# A tabulated solution with more space optmization is:
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        transactions = 2*k  # Considering 1 Buy and 1 Sell for each transaction
        curr = [ -1 for _ in range(transactions+1)]
        ahead = [0 for _ in range(transactions+1)]

        curr[transactions] = 0
        for idx in range(n-1, -1, -1):
            for trans in range(transactions-1, -1, -1):
                profit = 0
                if trans % 2 == 0: # Means buy time
                    profit = max(
                        -prices[idx] + ahead[trans + 1],
                        ahead[trans]
                    )
                else:
                    profit = max(
                        prices[idx] + ahead[trans + 1],
                        ahead[trans]
                    )
                curr[trans]= profit
            ahead = curr
        
        return ahead[0]