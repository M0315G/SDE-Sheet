from typing import List

# Question:
# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:
# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).
# Return the number of alternating groups.
# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.


# Logic:
# The logic is to use a sliding window approach to do this, we loop from 1 to n+k elements with idx = (idx +1)%n thus effectively looping around the array.
# Next, we keep a track of last color and check if the current one is simiar or not, if similar we reset, else increase the seq_len.

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        seq_len = 1
        last_color = colors[0]
        result = 0

        for idx in range(1, n + k -1):
            idx %= n

            if colors[idx] == last_color:
                seq_len = 1
                last_color = colors[idx]
                continue
            
            seq_len += 1
            last_color = colors[idx]
            if seq_len >= k:
                result += 1
            
    
        return result
        