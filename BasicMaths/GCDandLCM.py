# Question:
# Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD.
# The function inputs two integers a and b and returns a list containing their LCM and GCD.

# Logic:
# Find the GCD using Eucledian's algorithm:
# gcd(a, b) = gcd(a%b, b) (a>b), we do this until a%b -> 0, then the answer is b
# and LCM = a*b//gcd, because max num can be a*b and gcd removes all the common factors.

from typing import List

class Solution:
    def gcd(self, a, b):
        while(a>0 and b>0):
            if a>b:
                a = a%b
            else:
                b = b%a
        if a == 0:
            return b
        return a

    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        hcf = self.gcd(a, b)
        return [a*b//hcf, hcf]