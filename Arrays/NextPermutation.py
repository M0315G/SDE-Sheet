from typing import List

# Question:
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Logic:
# We use 3 steps to do this:
# 1. Traverse the array from behind and try to find the break point --> break point is the index at which we find an element
#    such tht array[i] < arr[i+1] i.e. there is one element which is greater than the current index and thus we can swap the smaller element
#    with the next bigger element to get the "just" next biggest array.
#       --> if we dont find the break point that means the array is at it's max permutation, in that case just reverse it and send back.
#    For the array --> [1, 2, 3, 4, 3, 2, 1, 0] the breakpoint is the index 2 (0 based) it's value = 3. Thus we have to find the next biggest number
#       we can swap it with.
# 2. Find the smallest maximum element to swap i.e. in the array [1, 2, 3, 4, 3, 2, 1, 0] the breakpoint is index 2 = element 3 (0 based) and
#    the smallest maxium we can swap it with is 4 (3rd index). To find the smallest maximum, we again iterate from n-1 to index (in this case 2) and
#    try to find an element such that nums[i] > nums[index]. We swap them and then.
# 3. Take the reverse of the rest of the array i.e. [1, 2, 4, 3, 3, 2, 1] so take the reverse and it gives [1, 2, 4, 1, 2, 3, 3].


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for idx in range(len(nums)-2, 0, -1):
            if nums[idx] < nums[idx+1]:
                index = idx
                break

        if index != -1:
            for idx in range(len(nums)-1, index, -1):
                if nums[idx] > nums[index]:
                    tmp = nums[index]
                    nums[index] = nums[idx]
                    nums[idx] = tmp
                    break
            
            part_2 = nums[index:][::-1]
            answer = nums[:index] + part_2
            return answer
        else:
            return nums[::-1]
