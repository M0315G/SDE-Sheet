from typing import List

# Question:
# You are given a 0-indexed array of strings words and a 2D array of integers queries.
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

# Logic:
# We do 1 pass and store the no of such strings we can find upto that index in that array.
# Thus when we iterate over the ranges, we just calculate the difference between the right - (left) positions.

class Solution:
    def check_if_vowel(self, word) -> bool:
        f = word[0]
        l = word[-1]
        if f == "a" or f =="e" or f == "i" or f == "o" or f == "u":
            if l == "a" or l =="e" or l == "i" or l == "o" or l == "u":
                return True
        return False

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = [1 if self.check_if_vowel(words[0]) else 0]
        # Create the array to store the no of strings which satisfy the criteria.
        for i in range(1, len(words)):
            cnt = vowel[i-1]
            if self.check_if_vowel(words[i]):
                cnt += 1
            vowel.append(cnt)
        print(vowel)
        ans = []
        # Now we iterate over each range if it doesn't start with 0, we calculate the total strings as:
        # -> vowel[right] - vowel[left - 1] we do a -1 bcos the left index is also inclusive.
        for i in range(len(queries)):
            left, right = queries[i][0], queries[i][1]
            if left == 0:
                ans.append(vowel[right])
            else:
                ans.append(vowel[right]-vowel[left-1])
        return ans
        