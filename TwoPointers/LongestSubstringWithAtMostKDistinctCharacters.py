# Question:
# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

# Logic:
# Same logic as in Fruits into basket, here 2 is replaced by k.

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right = 0, 0
        charMap = defaultdict(int)
        n = len(s)
        maxLen = 0
        while right < n:
            charMap[s[right]] += 1
            if len(charMap.keys()) > k:
                charMap[s[left]] -= 1
                if charMap[s[left]] == 0:
                    del charMap[s[left]]
                left += 1
            else:
                maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen