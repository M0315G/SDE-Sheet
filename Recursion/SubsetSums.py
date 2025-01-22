from typing import List

# Question:
# Given a array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.

# Logic:
# To solve it using recursion we use a very simple option: to pick or not to pick.

class Solution:
    def subsum(self, arr, index, currSum, answer):
        if index == len(arr):
            answer.append(currSum)
            return
        
        self.subsum(arr, index+1, currSum + arr[index], answer)
        self.subsum(arr, index+1, currSum, answer)

    def subsetSums(self, arr):
		# code here
        answer = []
        self.subsum(arr, 0, 0, answer)
        return answer