# Question:
# Given an array arr[] containing positive elements, the task is to find the length
# of the longest subarray of an input array containing at most two distinct integers.

# Logic:
# We use the same optimization logic as used in the "Longest subarray/substring with <condition>"
# We keep a hashmap for all the values and their frequencies.
# We keep adding hasmap[right] += 1
# If the size of the hashmap grows > 2:
#       we subtract 1 from the freq of hasmap[left] and increment it
#       if hashmap[left] ==0: we delete that key (thus making it of length 2 again)

from collections import defaultdict
class Solution:
    def totalElements(self,arr):
        left, right = 0, 0
        maxLen = 0
        s = defaultdict(int)
        n = len(arr)
        while right < n:
            s[arr[right]] += 1
            if len(s.keys()) > 2:
                s[arr[left]] -= 1
                if s[arr[left]] == 0:
                    del s[arr[left]]
                left += 1
            else:
                maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen