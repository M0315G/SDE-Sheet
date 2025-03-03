# Question:
# Given an array arr[], partition it into two subsets(possibly empty) such that each element must belong to only
# one subset. Let the sum of the elements of these two subsets be sum1 and sum2. Given a difference d, count the number
# of partitions in which sum1 is greater than or equal to sum2 and the difference between sum1 and sum2 is equal to d. 

# Logic:
# There is a simple way to convert this into the count of subset with sum = k, how?
# Since s1-s2=d and s1 = totalSum - s2
# we get totalSum - s2 - s2 = d => s2 = (totalSum - d)/2
# Thus we find the no of subsets with sum == s2
# Some base cases handling the zeros (where sum == 0 and values in arr can be 0)
# In recursion the base case would be:
#       if index == 0:
#           if sum == 0 and nums[0] == 0: return 2
#           if sum == 0 or nums[0] == sum: return 1
#           return 0

# This translates to:
# if nums[0] == 0:
#   prev[0] = 2 (since it's already zero it'll help in creating a zero sum as well as any other sum)
# else:
#   prev[0] = 1 (bcos of the case when sum==0)
# and in the next condition arr[0] <= target, just check that arr[0] !=0 bcos then it'll override the above if condition.

class Solution:
    def countPartitions(self, arr, d):
        n = len(arr)
        totalSum, zeros = 0, 0
        for num in arr:
            totalSum += num
            if num == 0:
                zeros += 1
        
        reqSum = (totalSum - d)
        if reqSum < 0 or reqSum%2 != 0:
            return 0
        reqSum = int(reqSum/2)
        prev = [0 for _ in range(reqSum+1)]
        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1

        if arr[0] != 0 and arr[0] <= reqSum:
            prev[arr[0]] = 1
        
        for k in range(1, n):
            curr = [0 for _ in range(reqSum+1)]
            for target in range(reqSum+1):
                not_pick = prev[target]
                pick = 0
                if arr[k] <= target:
                    pick = prev[target - arr[k]]
                curr[target] = pick + not_pick
            prev = curr
        
        return prev[reqSum]