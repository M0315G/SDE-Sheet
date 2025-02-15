# Question:
# You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i
# and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single
# meeting room, when only one meeting can be held in the meeting room at a particular time. 
# Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

# Logic:
# We sort the meetings based on their ending time and then take all the ones which do not overlap.

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        meetings = []
        for idx in range(len(start)):
            meetings.append([idx, start[idx], end[idx]])
        meetings = sorted(meetings, key= lambda x: x[2])
        freeTime = meetings[0][2]
        order = [meetings[0][0]]
        for meet in meetings[1:]:
            if meet[1] > freeTime:
                order.append(meet[0])
                freeTime = meet[2]
        return len(order)