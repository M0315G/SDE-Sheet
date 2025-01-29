from typing import Optional

# Question
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Logic:
# We just do a Preorder iterative traversal and if any point the structure seems different then we return False.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            if q:
                return False
            else:
                return True
        if not q:
            if p:
                return False
            else:
                return True
        st = []
        st.append([p, q])
        while len(st)!=0:
            left, right = st.pop(-1)
            if left.val != right.val:
                return False
            if left.right:
                if not right.right:
                    return False
                st.append([left.right, right.right])
            elif right.right:
                return False
            if left.left:
                if not right.left:
                    return False
                st.append([left.left, right.left])
            elif right.left:
                return False
        return True

        