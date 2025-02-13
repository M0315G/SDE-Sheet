# Question:
# You are given three arrays: id, deadline, and profit, where each job is associated with an ID, a deadline, and a profit.
# Each job takes 1 unit of time to complete, and only one job can be scheduled at a time.
# You will earn the profit associated with a job only if it is completed by its deadline.
# Your task is to find:
# 1. The maximum number of jobs that can be completed within their deadlines.
# 2. The total maximum profit earned by completing those jobs.

# Logic:
# Sort the jobs by profit and then try to allocate each job.
# While allocating make sure to allocate it as late as possible i.e. on the day of the dealine, if not possible iterate back to find
# an available slot.

# Note: Revisit the code after learning DSU in graph to optimize the inner for loop to O(1) solution

class Solution:
    # Function used for sorting jobs according to their deadlines
    def JobSequencing(self, id, deadline, profit):
        combinedArr = []
        for x, y, z in zip(id, deadline, profit):
            combinedArr.append([x, y, z])
        
        combinedArr = sorted(combinedArr, key=lambda x: x[2], reverse=True)
        maxDays = max(deadline)
        jobArr = [-1]*(maxDays+1)
        maxProfit = 0
        jobs = 0
        # print(jobArr)
        for x, y, z in combinedArr:
            idx = y
            # print(idx)
            while idx >= 0 and jobArr[idx]!=-1:
                idx -= 1
            if idx > 0:
                jobArr[idx] = x
                maxProfit += z
                jobs += 1
        return [jobs, maxProfit]