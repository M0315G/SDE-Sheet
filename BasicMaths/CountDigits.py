# Question:
# Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder). Return the total number of such digits.
# A digit d of n divides n evenly if the remainder when n is divided by d is 0 (n % d == 0).
# Digits of n should be checked individually. If a digit is 0, it should be ignored because division by 0 is undefined.

# Logic:
# Iterate over all the digits of the number and check if it divides it or not.

class Solution:
    def evenlyDivides(self, n):
        count = 0
        original = n
        while(n>0):
            num = n%10
            if num!=0 and original%num == 0:
                count += 1
            n = int(n/10)
        return count