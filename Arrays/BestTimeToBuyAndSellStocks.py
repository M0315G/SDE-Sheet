from typing import List

# Question:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Logic:
# We create a maxList which basically tell us that if we choose the element at position i, what's the maximum element we'll get on the right
# side of the array for it.
# This does the work in O(2n) time and O(n) space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        maxList = [prices[n-1]]
        for i in range(n):
            currEle = prices[n-i-2]
            currMax = maxList[i]
            if currEle > currMax:
                maxList.append(currEle)
            else:
                maxList.append(currMax)
        maxList = maxList[::-1]
        for i in range(len(prices)-1):
            currMax = maxList[i+1]
            curr_profit = currMax - prices[i]
            if curr_profit > profit:
                profit = curr_profit
        return profit
    

# Approach 2:
# We maintain O(n) time complexity and O(1) space complexity:
# We take 2 variables: minVal(set to 1st element of array) and profit(start with 0)
# For each element in the array, we check:
# --> if the value is less than the minVal, if yes change minVal
# --> else check if current value - minVal > profit, if yes change the profit value
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