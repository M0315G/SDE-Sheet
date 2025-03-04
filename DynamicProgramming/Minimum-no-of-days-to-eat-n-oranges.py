# Question:
# There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:
# Eat one orange.
# If the number of remaining oranges n is divisible by 2 then you can eat n / 2 oranges.
# If the number of remaining oranges n is divisible by 3 then you can eat 2 * (n / 3) oranges.
# You can only choose one of the actions per day.

# Given the integer n, return the minimum number of days to eat n oranges.


# Logic:
# This problem deserves a special mention bcos of 2 things:
# The logic to solve this is simple, we do pick or not pick on all 3 possible outcomes for each day but because of the extremes of the test-cases
# we're forced to do 2 optimizations:
# 1. use hashdict instead of array to avoid storing numbers which never occur.
# 2. use an intelligent way to do n-1 (see the comment in the solution below) to avoid TLE.

from collections import defaultdict
class Solution:
    def minDays(self, n: int) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        dp[1] = 1

        def choose(n):
            if n in dp:
                return dp[n]
            # This logic works as follows:
            # We are still choosing between doing -1, -n/2 or -2*(n/3) but
            # repeatedly calling -1 gives TLE so instead we do n%2 and n%3 bcos
            # that's the amount of -1 we'll have to do to get to a 'n' which is either
            # divisible by 2 or by 3.
            dp[n] = 1 + min(n%2 + choose(n//2), n%3 + choose(n//3))
            return dp[n]

        return choose(n)
        