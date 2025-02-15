from typing import List

# Question:
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of
# the non-overlapping intervals that cover all the intervals in the input.

# Logic:
# We sort the intervals and then iterate over them and if the current one overlaps with the old one, we update it.

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