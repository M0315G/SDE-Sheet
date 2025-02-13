# Question:
# Geek is a software engineer. He is assigned with the task of calculating average waiting time of all the processes by
# following shortest job first policy.
# The shortest job first (SJF) or shortest job next, is a scheduling policy that selects the waiting process with the
# smallest execution time to execute next.
# Given an array of integers bt of size n. Array bt denotes the burst time of each process. Calculate the average waiting
# time of all the processes and return the nearest integer which is smaller or equal to the output.
# Note: Consider all process are available at time 0.

# Logic:
# Sort and add all waiting times.

import math
class Solution:
    def solve(self, bt):
        bt.sort()
        wt_time, t = 0, 0
        for idx in range(len(bt)):
            wt_time += t
            t += bt[idx]
            # print(wt_time, t, bt[idx])
        return math.floor(wt_time/len(bt))