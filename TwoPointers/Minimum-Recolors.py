# Question:
# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
# You are also given an integer k, which is the desired number of consecutive black blocks.
# In one operation, you can recolor a white block such that it becomes a black block.
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

# Logic:
# A standard 2 pointer sliding window solution, we increment right and when the len is == k, we calculate the min no of swaps.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        num_recolors = float('inf')
        num_whites = 0

        for right in range(len(blocks)):

            if blocks[right] == 'W':
                num_whites += 1
            if right - left + 1 == k:
                num_recolors = min(num_recolors, num_whites)
                if blocks[left] == 'W':
                    num_whites -= 1
                left += 1
        return num_recolors