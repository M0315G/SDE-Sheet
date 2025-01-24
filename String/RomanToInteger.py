# Question:
# Given a roman numeral, convert it to an integer.

# Logic:
# Keep a hash map for the different roman numbers. Now only the tricky parts are IV(5), IX(9), XL(49) --> but if we observe carefully here a smaller
# number follows a bigger number i.e I before V or X, X before L, thus we iterate at 2 numbers at a time and see which one is smaller.

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                res += roman[a]

        return res + roman[s[-1]]