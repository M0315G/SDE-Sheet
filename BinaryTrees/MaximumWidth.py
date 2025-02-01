from typing import Optional

# Question
# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.

# Logic:
# See the video: --> https://www.youtube.com/watch?v=ZbybYvcVLks

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st = []
        maxWidth = 0
        st.append([0, root])
        while len(st)!=0:
            n = len(st)
            mmin = st[0][0]
            first, last = 0, 0
            for i in range(n):
                x, curr = st.pop(0)
                curr_min = x - mmin
                if i==0:
                    first = curr_min
                if i == n-1:
                    last = curr_min
                if curr.left:
                    st.append([curr_min*2+1, curr.left])
                if curr.right:
                    st.append([curr_min*2+2, curr.right])
            maxWidth = max(maxWidth, last-first+1)
        return maxWidth
                