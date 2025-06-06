from collections import defaultdict
# Question:
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
# character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

# Logic:
# We use a hasmap to keep track of characters in an interesting way. See the video --> https://www.youtube.com/watch?v=WJaij9ffOIY&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=12
# Dry run the logic against this test case: (makes it easier to understand)
# s = "ddaaabbca" t = "abc"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charMap = defaultdict(int)
        for ch in t:
            charMap[ch] += 1
        left, right = 0, 0
        minLen = float('inf')
        startIndex = -1
        count = 0
        x = len(t)
        while right < len(s):
            if charMap[s[right]] > 0:
                count += 1
            charMap[s[right]] -= 1

            while count == x:
                if right - left + 1 < minLen:
                    startIndex = left
                    minLen = right - left + 1
                charMap[s[left]] += 1
                if charMap[s[left]] > 0:
                    count -= 1
                left += 1

            right += 1
        
        if startIndex == -1:
            return ""
        return s[startIndex: startIndex + minLen]
            
