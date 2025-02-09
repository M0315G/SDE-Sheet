# Question:
# You are given a string s and an integer k. You can choose any character of the string and change it to any other
# uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.


# Logic:
# The only novel thing here is to create a formula which we can compare with k, thus the maximum amount of modifications needed in any
# substring of length L should be less than k, which means the frequency of the element which is appearing the most in that substring should
# be atleast L-k, which gives us:
#   currLen(L) - maxFreq <=k for us to be able to replace the remaining characters to make it a valid string.
# Now we take this formula and apply it to the same 2 pointer sliding window approach.
# increment r every time, if the above condition is false, increment l once. --> why only once? watch the video to understand.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        maxLen = 0
        n = len(s)
        maxFreq = {}
        maxF = 0
        while right < n:
            if s[right] not in maxFreq.keys():
                maxFreq[s[right]] = 1
            else:
                maxFreq[s[right]] += 1

            maxF = max(maxF, maxFreq[s[right]])
            length = (right - left + 1)

            if length - maxF <= k:
                maxLen = max(maxLen, length)
            else:
                maxFreq[s[left]] -= 1
                left += 1
            right += 1
        return maxLen

