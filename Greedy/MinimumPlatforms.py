# Question:
# You are given the arrival times arr[] and departure times dep[] of all trains that arrive at a railway station on
# the same day. Your task is to determine the minimum number of platforms required at the station to ensure that no train is kept waiting.
# At any given time, the same platform cannot be used for both the arrival of one train and the departure of another. Therefore,
# when two trains arrive at the same time, or when one arrives before another departs, additional platforms are required to
# accommodate both trains.


# Logic:
# We sort both the arrays of arrival and dept and iterate using 2 pointers. if we find a train is arriving before the current departure, we
# need 1 more platform, if not 1 platform is getting free (-1).

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort(), dep.sort()
        
        maxPlatform = 0
        currPlatform = 0
        left, right = 0, 0
        while left < len(arr):
            if arr[left] <= dep[right]:
                currPlatform += 1
                left += 1
            else:
                currPlatform -= 1
                right += 1
            
            maxPlatform = max(maxPlatform, currPlatform)
            
        
        return maxPlatform