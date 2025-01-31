from typing import List, Optional

# Question:
# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# Answer:
# We do the level order traversal and insert the children from right to left.
# Then we just need the node at the 0th index at every level.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        ans = []
        if not root:
            return ans
        st.append(root)
        while len(st)!=0:
            n = len(st)
            for i in range(n):
                curr = st.pop(0)
                if i==0:
                    ans.append(curr.val)
                if curr.right:
                    st.append(curr.right)
                if curr.left:
                    st.append(curr.left)
        return ans