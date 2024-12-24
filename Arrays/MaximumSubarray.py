from typing import List

# Question:
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Logic:
# 1. The brute force method is to calculate the sum for all sub-arrays and just return the maximum of it.
# 2. The optimized one is an O(n) solution also known as Kadane's algorithm:
        # --> We keep on adding the numbers while iterating through the array.
        # --> Key thing is to not carry the summations < 0 i.e. if the first element is -3, thus the sum will be -3 so we'll drop it and reinitialize the sum to 0.
        # --> Doing this makes sure that we dont carry forward summations which are negative bcos it will never add value, it'll always eat more.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
        return maxSum


# Another alteration to this is to return the maximum subarray.

# Logic:
# We just add a way to maintain the indices in our optimized logic.
#   --> Note that whenever we're starting with a new subarray the value of summation is always 0 --> thus this will give us the start index.
#   --> Now, the subarray we find is only useful if the summatiom > maxSum we've found till now thus we only update the start and end indices when this condition occurs.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        currSum = 0
        start = -1
        arrStart, arrEnd = -1, -1
        for i in range(len(nums)):
            if currSum == 0:
                start = i
            currSum += nums[i]

            if currSum > maxSum:
                maxSum = currSum
                # We update the indices here bcos this subarray is important to us.
                arrStart = start
                arrEnd = i
            if currSum < 0:
                currSum = 0

        return nums[arrStart: arrEnd +1]