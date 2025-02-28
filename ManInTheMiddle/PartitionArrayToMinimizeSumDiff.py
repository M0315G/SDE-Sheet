from typing import List
import bisect
from itertools import combinations

# Question:
# You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of
# length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.
# Return the minimum possible absolute difference.

# Logic:
# Read ClosestSubsequentSum.py as a pre-requisite.
# After that the only difference here is since we want to partition the array, we calculate the sum as the combination of index i.e.
# the output sum is:
# {
#   1: [2, 5, 7], i.e. if we take only 1 element from the array
#   2: [7, 9, 12],  i.e. if the take only 2 elements from the array
#   3: [14] i.e. take al 3
# }

# We need this kind of output bcos we need to decide weather to take 1 element from left subraay and remaining n-1 from right, or 2 from left and
# n-2 from right and so on.
# this we iterate on K being from 1---n-1 and see if we pick k elements from left subarray and n-k from right, what's the minimum sum we can get
# The inner for loop here: for x in left_part --> this is bcos when we're taking k element from left, there are multiple sum options (as we can see in the
#  sum dictionary above) thus we consider all sum options and find a relevant option in the right (using binary search) and then do the idx and idx-1 thing.

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def generate_sums(nums):
            sums = {}
            for k in range(1, len(nums) + 1):
                s = []
                for comb in combinations(nums, k):
                    s.append(sum(comb))
                sums[k] = s
            return sums
        
        n = len(nums)//2
        if n == 1:
            return abs(nums[0] - nums[1])
        left, right = nums[:n], nums[n:]
        left_sums, right_sums = generate_sums(left), generate_sums(right)
        ans = abs(sum(left) - sum(right))
        total = sum(nums)
        half = total // 2      
        for k in range(1, n):
            left_part = left_sums[k]
            right_part = right_sums[n-k]
            right_part.sort()
            for x in left_part:
                target = half - x
                idx = bisect.bisect_left(right_part, target)
                for i in [idx, idx - 1]:
                    if 0 <= i < len(right_part):
                        l = x + right_part[i]
                        r = total - l
                        ans = min(ans, abs(l - r))
        return ans
