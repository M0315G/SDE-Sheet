
# Question:
# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Note that in your output A should precede B.

# Logic:
# First brute force solution would be to keep the frequency counts and then the one with freq=2 is repeated and with freq=0 is missing.
# For optimised solution, Solve using maths:
# --> we can create 2 equations for"
#   --> sum of array - sum of numbers from 1 to N ==> this gives us the equation for x-y=val1
#   --> sum of square of array - sum of square of numbers from 1 to N ==> this gives us the equation x^2 - y^2 = val2 which can modified to get x+y=val2
# The just solve these 2 equations.

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        sumN = float((n*(n+1))/2)
        sum2N = float((n*(n+1)*(2*n+1))/6)
        sum1, sum2 = 0.0, 0.0
        for i in range(n):
            sum1 += A[i]
            sum2 += float(A[i])*float(A[i])
        
        val1 = float(sum1 - sumN) # x - y value
        val2 = float(sum2 - sum2N) # x^2 - y^2 value
        val2 = float(val2/val1) # finding the value for x+y
        x = (val1 + val2)/2
        y = x - val1
        x = int(x)
        y = int(y)
        return [x, y]
