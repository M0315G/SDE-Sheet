# Question:
# Given a set of items, each with a weight and a value, represented by the array wt and val respectively. Also, a knapsack with a weight limit capacity.
# The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
# Note: Each item can be taken any number of times.

# Logic:
# Similar to 0/1 knapsack, just the difference being that we can take an item any number of times.
# We use the similar concept of Coin change - 1 where we can take any number of coins we want.

class Solution:
    def choose(self, wt, val, index, amount, dp):
        if index == 0:
            return (amount // wt[0])*val[0]
        
        if dp[index][amount] != -1:
            return dp[index][amount]
        
        not_pick = self.choose(wt, val, index-1, amount, dp)
        pick = 0
        if wt[index] <= amount:
            pick = self.choose(wt, val, index, amount - wt[index], dp) + val[index]
        
        dp[index][amount] = max(pick, not_pick)
        return dp[index][amount]
    
    
    def knapSack(self, val, wt,capacity):
        n = len(val)
        dp = [[-1 for _ in range(capacity+1)] for _ in range(n)]
        return self.choose(wt, val, n-1, capacity, dp)
    
# Tabulation approach

class Solution:

    def knapSack(self, val, wt,capacity):
        n = len(val)
        dp = [[-1 for _ in range(capacity+1)] for _ in range(n)]
        for t in range(0, capacity+1):
            multiplier = t//wt[0]
            dp[0][t] = multiplier*val[0]

        for idx in range(1, n):
            for target in range(capacity+1):
                not_pick = dp[idx-1][target]
                pick = 0
                if wt[idx] <= target:
                    pick = dp[idx][target - wt[idx]] + val[idx]
                dp[idx][target] = max(pick, not_pick)

        return dp[n-1][capacity]