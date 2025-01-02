from typing import List

# Question:
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Logic:
# --> Brute force would be O(N^2) where we take each element and try to find the maximum sequence we can create with them.
# --> Better solution would be to sort it and then try to find the maximum sequence; time complexity -> O(NlogN)
# --> Optimised solution is to push everything in a set data structure and take use of their O(1) or O(logN) find operation.
#       --> we take each element and work on the principle that if it's not a starting element we ignore it. i.e. if array has 100, 101, 102; 100 is considered the starting element of the LCS.
#       --> Then when a starting element is found we try to find the maximum longest sequence we can create from it.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ds = set()
        lcs = 0
        for i in range(len(nums)):
            ds.add(nums[i])
        
        for x in ds:
            # If x-1 is not there means it's a starting element.
            if x - 1 not in ds:
                cnt = 1
                # We iterate until we can find the next element in the set and keep on checking the max size.
                while x + 1 in ds:
                    cnt += 1
                    x += 1
                lcs = max(lcs, cnt)
        return lcs