from typing import List

# Question:
# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

# Logic:
# Since the condition here asks us to take numbers either from the left or the right, we cannot directly apply a simple two pointer approach across the array.
# As a result, we start by picking k elements from the left and keep on decreasing it by 1 and adding 1 right most element.
# We check sum each time and update if it crosses max.

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        left, right = k-1, n-1
        currSum = sum(cardPoints[0: left + 1])
        maxSum = currSum
        # print(currSum, maxSum)
        for i in range(1, k+1):
            currSum -= cardPoints[left]
            left -= 1
            currSum += cardPoints[right]
            right -= 1
            # print(currSum)
            if currSum > maxSum:
                maxSum = currSum
        return maxSum