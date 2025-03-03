# Question:
# Given an integer array height[] where height[i] represents the height of the i-th stair, a frog starts from the
# first stair and wants to reach the top. From any stair i, the frog has two options: it can either jump to the (i+1)th stair
# or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs. Determine the minimum
# total cost required for the frog to reach the top.

# Logic:
# Writing the most optimized  version of this problem since the 1 & 2 approaches are similar to CountStairs.
# We take prev2 = 0 (since the frog is already at 1st step) and prev1 = abs(height[1] - height[0])
# Now we iterate and find the next minimum cost.

class Solution:
    def minCost(self, height):
        if len(height) < 2:
            return 0
        prev2 = 0
        prev1 = abs(height[1] - height[0])
        for i in range(2, len(height)):
            curr = min( abs(height[i] - height[i-1]) + prev1, abs(height[i] - height[i-2]) + prev2 )
            prev2 = prev1
            prev1 = curr
        return prev1