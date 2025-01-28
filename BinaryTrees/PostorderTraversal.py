from typing import List, Optional

# Question:
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Logic: Left-Right-Root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorder(self, node, arr):
        if not node:
            return
        self.postorder(node.left, arr)
        self.postorder(node.right, arr)
        arr.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        # Recursive
        # self.postorder(root, answer)

        # Iterative using 2 stacks
        if not root:
            return []
        st1, st2 = [], []
        st1.append(root)
        while len(st1) != 0:
            ele = st1[-1]
            st1.pop(-1)
            st2.append(ele)
            if ele.left:
                st1.append(ele.left)
            if ele.right:
                st1.append(ele.right)
        
        answer = []
        for i in range(len(st2)-1, -1, -1):
            answer.append(st2[i].val)
        return answer