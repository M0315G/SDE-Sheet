from typing import List

# Question:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Logic:
# We keep a track of the minimul amount to buy the stock and then also calculate the profit given the minimal amount for each day.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        minVal = prices[0]
        for i in range(1, n):
            if prices[i] < minVal:
                minVal = prices[i]
            if prices[i] - minVal > profit:
                profit = prices[i] - minVal
        return profit