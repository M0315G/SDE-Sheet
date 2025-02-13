from typing import List

# Question:
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
# if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Logic:
# We take the interval approach, i.e. take two pointers l & r and see what's the max we can jump considering all elements in that array.

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l, r = 0, 0
        n = len(nums)
        while r < n-1:
            maxJump = 0
            for i in range(l, r+1):
                if i + nums[i] > maxJump:
                    maxJump = i + nums[i]
            l = r + 1
            r = maxJump
            jumps += 1
        return jumps