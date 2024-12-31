from typing import List

# Question:
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# --> 0 <= a, b, c, d < n
# --> a, b, c, and d are distinct.
# --> nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Logic:
# --> Brute force is to use 4 for loops and check all the combinations.
# --> An optimised O(n^3) would be to use hashing to replace the inner for loop.
# --> Most optimised space and time solution takes the intuition from 2 sum problem:
#       --> same left, right pointer approach. We keep i and j fixed and then run these pointers

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = set({})
        nums = sorted(nums)
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, n-1
                while left < right:
                    pSum = nums[i] + nums[j]
                    pSum += nums[left]
                    pSum += nums[right]
                    if pSum == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while (left < right and nums[left]==nums[left-1]):
                            left += 1
                        while (left < right and nums[right]==nums[right+1]):
                            right -= 1
                    elif pSum < target:
                        left += 1
                    else:
                        right -= 1
        answer = []
        for x in ans:
            answer.append(list(x))
        return answer