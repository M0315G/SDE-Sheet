from typing import List

# Question:
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Logic:
# Use 2 pointer approach and whenever you get a number in nums2 that is less than nums1, insert it by shifting the array.

class Solution:
    def shift_and_add_element(self, nums: List[int], index: int, val: int):
        tmp = val
        for i in range(index, len(nums)):
            nums[i], tmp = tmp, nums[i]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1, pointer2 = 0, 0
        for i in range(m+n):
            if pointer2 >= n:
                break
            val1 = nums1[pointer1]
            val2 = nums2[pointer2]
            if val1 < val2:
                pointer1 += 1
            else:
                # print(f"Inserting {val2} at location: {pointer1}.")
                # print(f"The array is: {nums1}")
                self.shift_and_add_element(nums1, pointer1, val2)
                pointer1 += 1
                pointer2 += 1
        
        if pointer2 < n:
            rem = n-pointer2
            nums1[-rem:] = nums2[-rem:]
        