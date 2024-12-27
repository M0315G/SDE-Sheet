# Question:
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Logic:
# --> The brute force solution would be to add a recursive + DP (memoization) technique and recursively call right and down on each element of the matrix
#    --> once we get to a position that's out of the matrix we return 0, if we reach the destination we return 1
#    --> For any position, the final value will be (val of left recursion) + (val of right recursion)
#    --> We start it from (0, 0) position
#    --> Use of DP here is to store the values of the visited paths like if i visit (1,1) i'll store the value of it's final recursive output in my DP table and when i reach there again i'll just take the value from the table instead of doing the recursion again.

# Optimised solution comes from observation:
# We try to see the max length of the path we need to traverse --> that comes out to be m+n-2
# Thus the problem then becomes the combinatorics problem where we need to just place either R or D in the blank spaces.
# Since once either 1 of them is placed, the position of the other one is fixed i.e. if you fix all R's then the position of remaining blanks has to be filled by the D's, we just need to find the value of combination of either one of these placements
# And this is given by nCr where n = m+n-2 and r = m-1 or n-1 (whichever is shorter to save compute).

class Solution:
    def compute_n_C_r(self, n, r):
        ans = 1
        for i in range(r):
            ans *= (n-i)
            ans /= (i+1)
        return int(ans)

    def uniquePaths(self, m: int, n: int) -> int:
        total_steps = m+n-2
        right = n-1
        left = m-1
        r = 0
        if left < right:
            r = left
        else:
            r=right
        return self.compute_n_C_r(total_steps, r)
