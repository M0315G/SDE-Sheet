from typing import List

# Question
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations

# Logic:
# We borrow the logic from Subsets-2 problem where we iterate in a for loop to discard the duplicate elements.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(candidates)
        candidates = sorted(candidates)
        # print(candidates)
        def combinations(index: int, tar: int, curr: List[int]):
            # print(f"Called for index: {index} and tar: {tar} and curr: {curr}")
            if tar == 0:
                answer.append(curr)
                return
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > tar:
                    break
                combinations(i+1, tar - candidates[i], curr + [candidates[i]])
        combinations(0, target, [])
        return answer
         