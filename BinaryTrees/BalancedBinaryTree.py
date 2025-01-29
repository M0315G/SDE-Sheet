from typing import Optional

# Question:
# Given a binary tree, determine if it is height-balanced.

# Logic:
# We check the left and right height of each subtree of each node and if that height has a difference > 1 then it is unbalanced.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, node: Optional[TreeNode]) -> int:
        isbalanced = True
        if not node:
            return 0, isbalanced
        left, l = self.height(node.left)
        right, r = self.height(node.right)

        if abs(left - right) > 1 or not l or not r:
            isbalanced = False
        # print(left, right, isbalanced)
        return 1 + max(left, right), isbalanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, isbalanced = self.height(root)
        return isbalanced