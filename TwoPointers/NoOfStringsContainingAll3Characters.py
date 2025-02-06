# Question:
# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

# Logic:
# Keep a hashmap of each character i.e. a, b, c
# As soon as we iterate, check if we have all the 3 characters (i.e. min value of index would not be -1)
# If found, add minVal + 1 to the answer bcos:
#       --> we can max a valid substring from index minVal to idx (current index) then we can include all the other substrings that are made by
#           adding the characters which are on left of minVal
#   For ex:
#     in string ababa[abbc]ba, for the substring from index 5 to 8 make a valid substring, so if we add character an index 0, 1, 2, 3, 4 also then it'll
#      still be a valid substring

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = {
            "a": -1,
            "b": -1,
            "c": -1,
        }
        ans = 0
        for idx in range(len(s)):
            ch = s[idx]
            pos[ch] = idx
            minVal = min(pos.values())
            if minVal != -1:
                ans += minVal + 1
        return ans