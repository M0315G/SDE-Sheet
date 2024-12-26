from typing import List

# Question
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Logic:
# --> Brute force solution would be to maintain frequency of each element and then as soon as any one goes > n/2 we get it as answer.
# --> Optimised solution is Moore's voting: We maintain 2 variables element and count: watch YT video to understand.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = -1
        count = 0
        for i in range(len(nums)):
            if count == 0:
                count = 1
                ele = nums[i]
            elif ele == nums[i]:
                count += 1
            else:
                count -= 1
        return ele