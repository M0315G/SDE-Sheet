# Question:
# Geek is going for a training program for n days. He can perform any of these activities: Running, Fighting, and
# Learning Practice. Each activity has some point on each day. As Geek wants to improve all his skills, he can't do the
# same activity on two consecutive days. Given a 2D array arr[][] of size n where arr[i][0], arr[i][1], and arr[i][2]
# represent the merit points for Running, Fighting, and Learning on the i-th day, determine the maximum total merit points Geek can achieve .

# Logic:
# To solve it using DP we have 3 ways:
# 1. Recursion with Memoization:
#   --> We traverse through every possible case and keep a 2D DP array of dp[day][last_Action] to reduce the time complexity.

class Solution:
    def collect(self, arr, day, last, dp):
        if dp[day][last] != -1:
            return dp[day][last]

        if day == 0:
            maxPoints = 0
            for i in range(3):
                if i != last:
                    maxPoints = max(maxPoints, arr[0][i])
            dp[day][last] = maxPoints
            return maxPoints

        maxPoints = 0
        for i in range(3):
            if i != last:
                maxPoints = max(
                    maxPoints,
                    arr[day][i] + self.collect(arr, day - 1, i, dp)
                )
        dp[day][last] = maxPoints
        return maxPoints

    def maximumPoints(self, arr):
        n = len(arr)
        dp = [[-1 for _ in range(4)] for _ in range(n+1)]
        return self.collect(arr, n-1, 3, dp)