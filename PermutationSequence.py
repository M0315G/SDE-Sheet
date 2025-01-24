# Question
# Given n and k, return the kth permutation sequence.

# Logic:
# Brute force would be to generate all possible permutations and then pick the kth one --> but this gives the time complexity of O(n!)
# Optimised one is to find the exact kth permutation. We do that by:
#   --> fix the 1st element, then we have (n-1)! permutations to navigate too --> by doing so determine for which 1st element the k fall in the given range
#   --> do this recursively for all places
# Watch Striver's video if the above explanation doesn't make sense.

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        nums = []
        for i in range(1, n):
            fact = fact*i
            nums.append(i)
        
        nums.append(n)
        answer = ""
        k = k-1
        while True:
            answer = answer + str(nums[int(k//fact)])
            nums.pop(int(k//fact))
            if len(nums) == 0:
                break
            k = k % fact
            fact = fact / len(nums)
        return answer

        