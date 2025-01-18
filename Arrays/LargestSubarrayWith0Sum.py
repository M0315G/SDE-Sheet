# Question:
# Given an array arr containing both positive and negative integers, the task is to compute the length of the largest subarray that has a sum of 0.

# Logic:
# The brute force would be to just do O(n^2) to create all subarrays with sum = 0 and then check.
# Better solution would be to use a hash-map. Here we save all the different sum we get by adding the elements and check if the current sum exists before in the
# hash-map. If yes then we can say that sub-array will give us the sum = 0.

class Solution:
    def maxLen(self, arr):
        sumDict = {}
        maxLen = 0
        currSum = 0
        for i in range(len(arr)):
            currSum += arr[i]
            if arr[i] == 0 and maxLen == 0:
                maxLen = 1

            if currSum == 0:
                maxLen = i+1
            
            if currSum in sumDict:
                index = sumDict[currSum]
                maxLen = max(maxLen, (i-index))
            else:
                sumDict[currSum] = i
        return maxLen