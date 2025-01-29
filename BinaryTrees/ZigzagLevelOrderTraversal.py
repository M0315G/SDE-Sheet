from typing import List, Optional

# Question
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).

# Logic:
# During the level order traversal we keep a boolean to know if we're supposed to go l to r or r to l
# and based on that we select the order of insertion of nodes in the stack.
# We also reverse the stack everytime we toggle the boolean.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        answer = []
        st = []
        st.append(root)
        lr = True
        while len(st)!=0:
            level = []
            n = len(st)
            for i in range(n):
                curr = st[i]
                level.append(curr.val)
                if lr:
                    if curr.left:
                        st.append(curr.left)
                    if curr.right:
                        st.append(curr.right)
                else:
                    if curr.right:
                        st.append(curr.right)
                    if curr.left:
                        st.append(curr.left)
            for i in range(n):
                st.pop(0)
            st = st[::-1]
            answer.append(level)
            lr = not lr
        return answer
