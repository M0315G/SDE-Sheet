from typing import List
# Question
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Logic:
# We use recursion coupled with a for loop to check for where we should exactly partition such that the substrings are palindrome in nature.
# Thus we check for each partition point if the LHS sub-string is a palindrome and if yes we partition it and call the function recursively.

import copy

class Solution:
    def isPalindrome(self, s: str, start: int, end: int):
        while(start <= end):
            if (s[start]!=s[end]):
                return False
            start +=1
            end -= 1
        return True

    def selectPartitions(self, s: str, index: int, part: List[str], answer: list):
        if index == len(s):
            answer.append(copy.deepcopy(part))
        
        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                part.append(s[index: i+1])
                self.selectPartitions(s, i+1, part, answer)
                part.pop()

    def partition(self, s: str) -> List[List[str]]:
        answer = []
        self.selectPartitions(s, 0, [], answer)
        return answer
