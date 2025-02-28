from typing import List
import bisect

# Question:
# You are given an integer array nums and an integer goal.
# You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is,
# if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).
# Return the minimum possible value of abs(sum - goal).
# Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.


# Logic:
# The algorithm used here is Man in the Middle, bcos
# 1. the value of n is big such that 2^n causes TLE in recursion
# 2. There are no overlapping subproblems in this case.

# We divide the array into 2 parts and then perform the recusion --> thus doing only 2^(n/2) which doesn't cause a TLE.
# Here when doing recusion, we find all the possible subsequence sums possible for the given half array.
# Next, we sort the right_sum array so that we can apply binary search on it
# We take element from left_sum and try to find the goal - left = target nearest target in right_sums.

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:

        def generate_sums(nums):
            sums = {0}
            for num in nums:
                new_sums = {x + num for x in sums}  # Compute new sums separately
                sums |= new_sums  # Merge into original set i.e. union of two sets
            return list(sums)
        
        n = len(nums)
        left, right = nums[:n//2], nums[n//2:]
        left_sums, right_sum = generate_sums(left), generate_sums(right)

        right_sum.sort()

        ans = float('inf')
        for sum1 in left_sums:
            target = goal - sum1
            idx = bisect.bisect_left(right_sum, target)

            # Now idx is the index of element >= target in the right_sums, which means:
            #  if found, 0 <= idx <= len(right_sums)
            # Now, to get the nearest value of goal, we need to caluclate sum
            # using right_sums[idx] and right_sums[idx - 1] because if right_sums[idx] == target
            # then we've hit gold but what if the number >>> target and the right_sums array has a
            # number very close to it but smaller than target, consider the case:
            # right_sums = [.... 7 9 101....] and the target is 10
            # idx will point to element 101 and doing 101 + sum1 will not give us the sum closest to goal
            # rather doing 9 + sum1 will give us the sum closest to the goal
            if idx < len(right_sum):
                ans = min(ans, abs(goal - (sum1 + right_sum[idx])))
            if idx > 0: # Because for idx == 0, we wont have idx - 1
                ans = min(ans, abs(goal - (sum1 + right_sum[idx - 1])))
        return ans

        