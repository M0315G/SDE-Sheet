# Question:
# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

# Logic:
#   --> Brute force solution is to do 2 for loops and find out the maximum sum.
#   --> More optimized solution is to iterate 1 time and store the max value of ones and then:
#       --> we consider the whole array as left array in the starting and as each index progresses we:
#           --> we deduct the value of s[i] from ones; if it's it'll deduct 1 and if it's 0 it'll stay the same
#           --> next we simultaneously count the no of zeros and modify the sum if it's the largest. 
#
#   --> Most optimised solution is for the equation No of zeros in left(a) + no of ones in right(b) = sum, we can write a as no of ones in total(c) - no of ones in left(d)
#        --> thus it becomes: sum = b + c-d; now everything just depends on the left substring so we iterate only 1 time and find the values.


class Solution:
    def maxScore(self, s: str) -> int:
        ones, zeros = 0, 0
        best = float("-inf")
        for i in range(len(s)-1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1
            best = max(best, zeros-ones)
    
        if s[-1] == "1":
            ones += 1
        return ones + best
