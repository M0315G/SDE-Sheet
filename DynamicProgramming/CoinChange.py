from typing import List

# Question:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be
# made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.


# Logic:
# Approach of pick or not_pick but this time since the supply of each coin is infinite, if we decide to pick, we still stay at the same index.

class Solution:
    def choose(self, coins, index, amount, dp):
        if index == 0:
            if amount % coins[index] == 0:
                dp[index][amount] = amount // coins[index]
            else:
                dp[index][amount] = float('inf')
            return dp[index][amount]
        
        if dp[index][amount] != -1:
            return dp[index][amount]
        
        not_pick = self.choose(coins, index-1, amount, dp)
        pick = float('inf')
        if coins[index] <= amount:
            pick = self.choose(coins, index, amount - coins[index], dp) + 1
        
        dp[index][amount] = min(pick, not_pick)
        return dp[index][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
        self.choose(coins, n-1, amount, dp)
        return dp[n-1][amount] if dp[n-1][amount] != float('inf') else -1