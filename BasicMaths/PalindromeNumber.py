# Question:
# Given an integer x, return true if x is a palindrome, and false otherwise.

# Logic:
# Find the reverse and compare.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverseNum = 0
        if x < 0:
            return False
        num = abs(x)
        while(num>0):
            n = num%10
            num = int(num/10)
            reverseNum = reverseNum*10 + n
        return reverseNum == x