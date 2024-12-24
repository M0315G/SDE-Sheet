from typing import List

# Question:
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Logic:
# The most brute force solution is to use any type of sorting algorithm.
# The next optimized approach is to simply count the number of 0, 1 and 2s and then replace them in-place.
#   --> this gives us an O(n) solution but it still can be optimized.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count1, count2, count3 = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count1 += 1
            elif nums[i] == 1:
                count2 += 1
            elif nums[i] == 2:
                count3 += 1
        
        for i in range(count1):
            nums[i] = 0
        for i in range(count1, count1+count2):
            nums[i] = 1
        for i in range(count1+count2, count1+count2+count3):
            nums[i] = 2
        
# Most optimal solution --> Dutch National Flag Algorithm:
# Trick is how to use the pointers low, mid and high
#   --> the array between mid and high is always un-sorted so we add cases on where to move the element such that it becomes sorted.
#   --> Explanation is too long to write: Watch YT video of striver to understand.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid = 0, 0
        high = len(nums) - 1
        while mid<=high:
            if nums[mid] == 0:
                tmp = nums[mid]
                nums[mid] = nums[low]
                nums[low] = tmp
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                tmp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = tmp
                high -= 1
        