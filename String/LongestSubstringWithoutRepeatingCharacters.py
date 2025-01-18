# Question:
# Given a string s, find the length of the longest substring without repeating characters.

# Logic:
# Brute force would be to iterate through all substrings and check for duplicacy.
# Better approach would be to keep a set and if we find an element which is in the set, we increment the left pointer until that element is removed.
# Optimal solution is to store the index of that character so that when we find a duplicate we just move left to index + 1 of the duplicate element.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charPos = {}
        left, right = 0, 0
        n = len(s)
        maxLen = 0
        while right < n:
            c = s[right]
            if charPos.get(c, None) is None:
                maxLen = max(maxLen, (right - left)+1)
                charPos[c] = right
            else:
                if charPos[c] < left:
                    charPos[c] = right
                    maxLen = max(maxLen, (right - left)+1)
                else:
                    left = charPos[c]+1
                    charPos[c] = right
                    maxLen = max(maxLen, (right - left)+1)
            right += 1
        return maxLen