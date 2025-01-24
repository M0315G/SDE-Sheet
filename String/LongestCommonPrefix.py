from typing import List

# Question:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Logic:
# iterate through all strings and keep the current longest prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            curr = strs[i]
            min_val = min(len(prefix), len(curr))
            prefix = prefix[:min_val]
            for j in range(min_val):
                if prefix[j] != curr[j]:
                    prefix = prefix[:j]
                    break
            if prefix == "":
                break
        return prefix
        