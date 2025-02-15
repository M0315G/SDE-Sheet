from typing import List

# Question:
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

# Logic:
# Sort the intervals by the end time and count all which do not coincide, return len() - count


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key= lambda x: x[1])
        freeTime = intervals[0][1]
        count = 1
        # print(intervals)
        for meet in intervals[1:]:
            if meet[0] >= freeTime:
                count += 1
                freeTime = meet[1]
                # print(meet)
        # print(count)
        return len(intervals) - count