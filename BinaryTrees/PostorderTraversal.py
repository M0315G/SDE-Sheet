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
        self.postorder(root, answer)
        return answer