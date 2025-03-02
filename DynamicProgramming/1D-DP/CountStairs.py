# Question:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Logic:
# 1. Memoization:
#   --> we recursively traverse the stack with the rule f(n) = f(n-1) + f(n-2) where f(n) denotes the number of ways to reach to step n.
#       Base case: f(0) = 1

class Solution:
    def climb(self, n, dp):
        if n < 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.climb(n-1, dp) + self.climb(n-2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0] = 1
        return self.climb(n, dp)
        
# 2. Tabulation:
#   --> We take the bottom up approach and assign dp[0] amnd dp[1] = 1 and then build forward with the loop dp[n] = dp[n-1] + dp[n-2]

def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# 3. Optimsed:
#   --> We take the bottom up approach and assign prev1 amnd prev2 = 1 and then build forward with the loop curr = prev1 + prev2
#       then update prev2 = prev1 and prev1 = curr

def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 1
        for i in range(2, n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1