# Question:
# Given an array of integers A and an integer B.
# Find the total number of subarrays having bitwise XOR of all elements equals to B.

# Logic:
# Brute force would be to do O(n^2) iterations and check for every subarray.
# Optimal solution would be to store each XOR value in a dict along with the it's apperance count. Then for every iteration we check if we can get currXOR^B in the dict,
# if yes, then we increment by that count.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        xorCount = {0: 1}
        n = len(A)
        currXor = 0
        cnt = 0
        for i in range(n):
            currXor ^= A[i]
            x = currXor^B
            if xorCount.get(x, None) is not None:
                cnt += xorCount[x]
            
            if xorCount.get(currXor, None) is not None:
                xorCount[currXor] += 1
            else:
                xorCount[currXor] = 1
        return cnt
