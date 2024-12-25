from typing import List

# Question:
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Logic:
# Sort the interval array w.r.t the first element --> now you know adjacent intervals are close to each other.
# we just iterate over the whole array and check if the current low is less than the previous high, if so that interval needs to be merged.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda a: a[0])
        answer = []
        answer.append(intervals[0])
        idx = 0
        for i in range(1, len(intervals)):
            low, high = answer[idx][0], answer[idx][1]
            currLow = intervals[i][0]
            if currLow <= high:
                answer[idx][1] = max(intervals[i][1], answer[idx][1])
            else:
                answer.append(intervals[i])
                idx += 1
        return answer