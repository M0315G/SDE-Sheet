# Question:
# You are given the weights and values of items, and you need to put these items in a knapsack of capacity
# capacity to achieve the maximum total value in the knapsack. Each item is available in only one quantity.
# In other words, you are given two integer arrays val[] and wt[], which represent the values and weights associated
# with items, respectively. You are also given an integer capacity, which represents the knapsack capacity. Your
# task is to find the maximum sum of values of a subset of val[] such that the sum of the weights of the corresponding
# subset is less than or equal to capacity. You cannot break an item; you must either pick the entire item or leave it (0-1 property).


# Logic:
# This problem is again one of the classic DP on sequence problems, the algorithm to use here is "pick" or "not_pick" with a
# twist of using max of either of them since you cannot do both, so whatever choice gives you maximum reward, you choose that.
# Below is the memoization approach of the same:

class Solution:
    def assign(self, val, wt, index, dp, capacity):
        if capacity == 0:
            return 0
        if index == 0:
            if wt[index] <= capacity:
                return val[index]
            else:
                return 0
        
        if dp[index][capacity] != -1:
            return dp[index][capacity]
        
        not_pick = self.assign(val, wt, index-1, dp, capacity)
        pick = 0
        if wt[index] <= capacity:
            pick = self.assign(val, wt, index-1, dp, capacity - wt[index]) + val[index]

        dp[index][capacity] = max(pick, not_pick)
        return dp[index][capacity]
    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        n = len(wt)
        dp = [[-1 for _ in range(capacity+1)] for _ in range(n)]
        return self.assign(val, wt, n-1, dp, capacity)