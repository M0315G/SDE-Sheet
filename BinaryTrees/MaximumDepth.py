from typing import Optional

# This is also called the height of the Binary Tree.

# Question:
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Logic:
# Recrusively traverse the tree starting from the left to the right and return the value as 1 + max(left, right).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root)