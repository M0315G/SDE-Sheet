from typing import List

# Question:
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times

# logic:
# Checkout MajorityElements.py --> same logic just using 4 variables instead of 2.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1, ele2 = float("-inf"), float("-inf")
        cnt1, cnt2 = 0, 0
        for i in range(len(nums)):
            if cnt1 == 0 and nums[i] != ele2:
                cnt1 += 1
                ele1 = nums[i]
            elif cnt2 == 0 and nums[i] != ele1:
                cnt2 += 1
                ele2 = nums[i]
            elif ele1 == nums[i]:
                cnt1 += 1
            elif ele2 == nums[i]:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1, cnt2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == ele1:
                cnt1 += 1
            if nums[i] == ele2:
                cnt2 += 1
        m = math.floor(len(nums)/3)
        ans = []
        if cnt1 > m:
            ans.append(int(ele1))
        if cnt2 > m:
            ans.append(int(ele2))
        return ans