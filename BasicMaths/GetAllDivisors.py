# Question:
# Given an integer N, find all the divisors of N.

# Logic:
# Iterate to sqrt(N) and check for each i, if found then (i, N/i) are divisors of N.

import math

class Solution:
	def allDivisors(self, n):
		divisors = []
		for i in range(1, int(math.sqrt(n))+1):
			if n%i == 0:
				divisors.append(i)
				if n/i != i:
					divisors.append(n/i)
		return divisors