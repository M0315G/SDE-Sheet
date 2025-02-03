from typing import List

# Question:
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Logic:
# The idea is to use a two pointer approach and convert the problem to finding out the subarray with maximum length which has k zeros.
# Thus we move right and see if we got a zero, we increment the count.
# When count > k, we move left ahead by 1 place but we do not stop the right, it still goes + 1 every iteration.
#  Now here the logic is tricky, we are not doing a while loop to move left to the position of 0 which can be removed but it happens naturally
#   due to the algo's nature. We just increment left and move ahead.
#   bcos count is still > k, it'll still prompt left to move ahead, if we encounter that left is at a 0, we only then reduce the count.
# 
# See the video:  https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4 if you're not clear.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, 0
        zeros = 0
        maxLen = 0
        while right < n:
            if nums[right] == 0:
                zeros += 1
            
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                
            else:
                maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen

        
