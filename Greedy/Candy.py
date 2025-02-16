from typing import List

# Question:
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# Logic:
# We have 2 approaches to do this:
# 1. We iterate through the array in left to right manner and maintain an array of candy for each children.
#    We use the basic formula if arr[i] > arr[i-1] then candy[i] = candy[i-1] + 1, else candy[i] = 1
#    To handle the right side, we do this process for right to left again, this time maintaining the max candy for the children i
#    Watch hole solution at: https://www.youtube.com/watch?v=IIqVFvKE6RY
# 2. We use a slope method, upward slope and downward slope. See the above video to understand.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        summation = 1
        i = 1
        n = len(ratings)
        while i < n:
            if ratings[i] == ratings[i-1]:
                summation += 1
                i += 1
                continue
            
            peak = 1
            while i < n and ratings[i] > ratings[i-1]:
                peak += 1
                summation += peak
                i += 1
            
            down = 1
            while i < n and ratings[i] < ratings[i-1]:
                summation += down
                i += 1
                down += 1
            
            if down > peak:
                summation += (down - peak)
        return summation