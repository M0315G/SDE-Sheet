# Question:
# Given two positive integers n and x.
# Return the number of ways n can be expressed as the sum of the xth power of unique positive integers,
# in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1^x + n2^x + ... + nk^x.
# Since the result can be very large, return it modulo 10^9 + 7.
# For example, if n = 160 and x = 3, one way to express n is n = 2^3 + 3^3 + 5^3.

# Logic:
# Use the same pick or not_pick approach here to see which number's xth power you need to consider.
# Since all powers will be xth, we take the xth root of the number and use that as the max number.

class Solution:
    def findWays(self, num, target, x, dp):
        if target == 0:
            return 1

        if num == 1:
            if target == 1:
                return 1
            else:
                return 0

        if dp[num][target] != -1:
            return dp[num][target]
        
        not_pick = self.findWays(num-1, target, x, dp)
        pick = 0
        if num**x <= target:
            pick = self.findWays(num-1, target - num**x, x, dp)
        # print(f"For num: {num} at target: {target} we got: {pick} and {not_pick}")
        dp[num][target] = (pick + not_pick)%(10**9+7)
        return dp[num][target]

    def numberOfWays(self, n: int, x: int) -> int:
        num = int(n**(1/x)) + 1
        # print(n, x, num)
        dp = [[-1 for _ in range(n+1)] for _ in range(num+1)]
        return self.findWays(num, n, x, dp)%(10**9+7)