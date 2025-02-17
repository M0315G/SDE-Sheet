# Question:
# Given an array arr[] of size n, where arr[i] denotes the height of ith stone. Geek starts from stone 0 and from
# stone i, he can jump to stones i + 1, i + 2, … i + k. The cost for jumping from stone i to stone j is
# abs(arr[i] – arr[j]). Find the minimum cost for Geek to reach the last stone.

# Logic:
# Here we use the tabulation approach since the most optimized one will be equal to the tabulation approach in the worst time complexity.
# Idea is to keep an array dp of size n+1 and then for each element iterate from i-1, i-2, ... i-k and find the minimum cost of reaching i.

class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [0]*(n+1)
        for idx in range(1, n):
            minCost = float("inf")
            for j in range(1, k+1):
                if idx - j >= 0:
                    cost = dp[idx-j] + abs(arr[idx] - arr[idx-j])
                    minCost = min(minCost, cost)
            dp[idx] = minCost
        return dp[n-1]