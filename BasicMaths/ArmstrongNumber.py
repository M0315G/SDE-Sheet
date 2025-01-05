# Question
# Given a number x, determine whether the given number is Armstrong number or not.

# Logic:
# Take each digit and add it to the sum by * thrice and check if it's the same number at the end.

class Solution:
    def armstrongNumber(self, n):
        count = 0
        sum = 0
        original = n
        while(n>0):
            num = n%10
            n = int(n/10)
            sum += num*num*num
        return sum == original