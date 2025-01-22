from typing import List

# Question:
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Logic:
# This again comes down to recrusion and the basic pick and not-pick logic but the twist is since the elements can be picked multiple times, we
# keep the same index when we pick an element signaling that it can be picked more than once.
# Note: the solution here is not space optimized due to the currList + []  that I'm doing. It'll just create new lists everytime.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        def combine(index: int, tar: int, currList: List[int]):
            if index == n:
                if tar == 0:
                    result.append(currList)
                return
            
            print(index, currList, candidates[index], tar)
            if candidates[index] <= tar:
                # currList.append(candidates[index])
                combine(index, tar-candidates[index], currList + [candidates[index]])
                # currList.pop()
            combine(index+1, tar, currList)
        
        combine(0, target, [])
        return result