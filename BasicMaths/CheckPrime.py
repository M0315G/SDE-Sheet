# Question:
# Given an integer, check if the number is a prime or not.

# Logic:
# Check if there are any other divisors than 1, N; if yes then return False.

import math

class Solution:
	def checkPrime(self, n):
		divisors = []
		for i in range(2, int(math.sqrt(n))+1):
			if n%i == 0:
				return False
		return True