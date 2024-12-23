# Question:
# Given an input string s, reverse the order of the words.
# For example, the reverse of "  hello world  " is "world hello". (Look at how the extra spaces are removed)
# Logic:
#   1. Use the inbuilt .split of python to split by space and discard all the empty parts (i.e. the ones with "" string)

class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []
        for word in s.split(" "):
            if word:
                answer.append(word)
        return " ".join(answer[::-1])
        