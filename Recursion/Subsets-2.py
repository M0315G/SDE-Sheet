from typing import List

# Question:
# Given an integer array nums that may contain duplicates, return all possible subsets(the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Logic:
# Here, instead of the pick and not pick logic we use a for loop to filter out the duplicate entries.
# We sort the array first so that all duplicates are adjacent and then filter them.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums = sorted(nums)
        # print(nums)
        def subsets(index: int, currSubset: List[int]):
            result.append(currSubset)
            for i in range(index, n):
                if i != index and nums[i] == nums[i-1]:
                    continue
                subsets(i+1, currSubset + [nums[i]])
        
        subsets(0, [])
        return result