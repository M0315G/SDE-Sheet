from typing import Optional

# Question
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Logic:
# we use the same logic as that of the sametree.py. Here p & q are the left and right children of the root.
# Also since it's a mirror check and not similarity check, for every left child of p, we should compare the right child of q.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p, q = root.left, root.right
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
                if not right.left:
                    return False
                st.append([left.right, right.left])
            elif right.left:
                return False
            if left.left:
                if not right.right:
                    return False
                st.append([left.left, right.right])
            elif right.right:
                return False
        return True