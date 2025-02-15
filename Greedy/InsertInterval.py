from typing import List

# Question:
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the
# start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given
# an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
# still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.


# Logic:
# We break it down into 3 compartments, left, middle and right.
# Left & right are the ones with no overlap on left and right of the given interval.
# For middle, we iterate and get the minimum starting point and max end point for that interval.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        # Left part: Intervals which are shorter than the newInterval
        while (i < n and intervals[i][1] < newInterval[0]):
            result.append(intervals[i])
            i += 1
        
        # Middle part: Intervals which overlap with the newInterval
        while (i < n and intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Right part: Intervals which are bigger than the newInterval
        while (i < n):
            result.append(intervals[i])
            i += 1
        
        return result
