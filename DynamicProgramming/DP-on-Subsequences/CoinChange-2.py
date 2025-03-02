from typing import List

# Question:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

# Logic:
# This is just a modified version of Coin Change problem, here instead of minimum coins we're asked to give the total number of ways we can generate
# target. The DP remains same, we just replace it with counting of each valid combination instead of taking the minimum.

class Solution:
    def choose(self, coins, index, amount, dp):
        if index < 0:
            if amount == 0:
                return 1
            return 0
        
        if dp[index][amount] != -1:
            return dp[index][amount]
        
        not_pick = self.choose(coins, index-1, amount, dp)
        pick = 0
        if coins[index] <= amount:
            pick = self.choose(coins, index, amount - coins[index], dp)
        
        dp[index][amount] = pick + not_pick
        return dp[index][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
        dp[n-1][amount] = self.choose(coins, n-1, amount, dp)
        return dp[n-1][amount]


# Tabulation for the same:
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n)]
        for t in range(0, amount+1):
            if t % coins[0] == 0:
                dp[0][t] = 1

        for idx in range(1, n):
            for target in range(amount+1):
                not_pick = dp[idx-1][target]
                pick = 0
                if coins[idx] <= target:
                    pick = dp[idx][target - coins[idx]]
                dp[idx][target] = pick + not_pick

        return dp[n-1][amount]