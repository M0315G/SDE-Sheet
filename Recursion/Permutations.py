from typing import List
import copy

# Question:
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Logic:
# We can recrusively find all the possible permutations. The code below is brute force code with:
# Time complexity --> O(n!*n) and Space complexity --> O(n + n + n)

class Solution:
    def allpermute(self, curr: List[int], visited: dict, answer: List[List[int]]):
        if len(visited) == len(curr):
            answer.append(copy.deepcopy(curr))
            return
        
        for k, v in visited.items():
            if not v:
                curr.append(k)
                visited[k] = True
                self.allpermute(curr, visited, answer)
                visited[k] = False
                curr.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        visited = {}
        for i in nums:
            visited[i] = False
        self.allpermute([], visited, answer)
        return answer
    

# This solution is space optmised than the previous one. It uses only constant extra space for the index: O(1)
class Solution:
    def allpermute(self, index: int, nums: List[int], answer: List[List[int]]):
        if index == len(nums):
            answer.append(copy.deepcopy(nums))
            return
        
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.allpermute(index+1, nums, answer)
            nums[i], nums[index] = nums[index], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.allpermute(0, nums, answer)
        return answer