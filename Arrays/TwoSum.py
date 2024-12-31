from typing import List

# Question:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Logic:
# --> Brute force would be to do a double for loop with O(n^2) time complexity.
# --> More optimised solution would be to use a Hashmap (dict) to store the indexes and then wheneve you find a currNum + index = target we return the indexes.
# --> A more space optimized solution would be to sort the array and then use 2 pointers:
#       --> left starts from 0, right starts from n-1
#       --> if left + right < target; move left
#       --> if left + right > target; move right
#       --> if equal; return the index values

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(n):
            arr.append([nums[i], i])
        arr = sorted(arr)
        left, right = 0, n-1
        while left <= right:
            print(left, right)
            a1 = arr[left][0]
            a2 = arr[right][0]
            if a1 + a2 == target:
                return [arr[left][1], arr[right][1]]
            elif a1 + a2 < target:
                left += 1
            else:
                right -= 1