# Question:
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn)

# Logic:
# --> First brute force approach will be to just run the loop n times and multiply the value by itself.
# --> An optimised approach is:
#   --> We check if n%2==0; if yes then we can write the product as (x*x)^(n/2)
#   -->     And if not then we can write it as x*(x)^(n-1) which again makes the n divisible by 2 thus enabling the above formula.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = 1.0
        nn = float(n)
        if nn < 0:
            nn *= -1
        
        while nn > 0:
            if nn%2 == 0:
                x = x*x
                nn /= 2
            else:
                answer *= x
                nn -= 1
        if n<0:
            answer = float(1.0/answer)
        return answer
        