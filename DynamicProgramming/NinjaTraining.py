# Question:
# Geek is going for a training program for n days. He can perform any of these activities: Running, Fighting, and
# Learning Practice. Each activity has some point on each day. As Geek wants to improve all his skills, he can't do the
# same activity on two consecutive days. Given a 2D array arr[][] of size n where arr[i][0], arr[i][1], and arr[i][2]
# represent the merit points for Running, Fighting, and Learning on the i-th day, determine the maximum total merit points Geek can achieve .

# Logic:
# To solve it using DP we have 3 ways:
# 1. Recursion with Memoization:
#   --> We traverse through every possible case and keep a 2D DP array of dp[day][last_Action] to reduce the time complexity.
#       Recusive Formula:
#           f(day, last) = arr[day][i] + f(day + 1, i) for i in range(0, 1, 2) where i != last (i.e. we dont take the same action on consecutive days)

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

# 2. Tabulation:
#   --> We assign the initial values based on the 1st day and then keep on iterating for each day.

class Solution:
    def maximumPoints(self, arr):
        n = len(arr)
        dp = [[-1 for _ in range(4)] for _ in range(n+1)]
        dp[0][0] = max(arr[0][1], arr[0][2])
        dp[0][1] = max(arr[0][0], arr[0][2])
        dp[0][2] = max(arr[0][1], arr[0][0])
        dp[0][3] = max(arr[0][0], arr[0][1], arr[0][2])

        for day in range(1, n):
            for task in range(4):
                dp[day][task] = 0
                for i in range(3):
                    if i != task:
                        dp[day][task] = max(
                            dp[day][task],
                            arr[day][i] + dp[day-1][i]
                        )
        return dp[n-1][3]



# 3. Tabulation with optimized space complexity.
#   --> Instead of using 2D array we can just keep the 3 variables denoting the max points achieved until the n-1th day

class Solution:
    def maximumPoints(self, arr):
        n = len(arr)
        dp = [-1 for _ in range(4)]
        dp[0] = max(arr[0][1], arr[0][2])
        dp[1] = max(arr[0][0], arr[0][2])
        dp[2] = max(arr[0][1], arr[0][0])
        dp[3] = max(arr[0][0], arr[0][1], arr[0][2])

        for day in range(1, n):
            tmp = [-1]*4
            for task in range(4):
                for i in range(3):
                    if i != task:
                        tmp[task] = max(
                            tmp[task],
                            arr[day][i] + dp[i]
                        )
            dp = tmp
        return dp[3]