# Question:
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Logic:
# Take each number out of the current digit and add it to the revNum with the formula:
# revNum = revNum*10 + num

class Solution:
    def reverse(self, x: int) -> int:
        reverseNum = 0
        num = abs(x)
        while(num>0):
            n = num%10
            num = int(num/10)
            reverseNum = reverseNum*10 + n
            if reverseNum > 2**31 - 1:
                return 0
        if x > 0:
            return reverseNum
        else:
            return reverseNum*-1

        