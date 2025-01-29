from typing import Optional

# Question
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Logic:
# Diameter is essentially the sum of the height of left and right subtrees and thus we find the largest subtree to get the largest diameter.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0, 0, 0
        l1, r1, m1 = self.height(node.left)
        l2, r2, m2 = self.height(node.right)
        # print(l1, r1, node.val, "left")
        # print(l2, r2, node.val, "right")
        return 1 + max(l1, r1), 1 + max(l2, r2), max(max(l1,r1) + max(l2, r2), m1, m2)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l1, r1, m1 = self.height(root.left)
        l2, r2, m2 = self.height(root.right)
        # print(l1, r1, "left")
        # print(l2, r2, "right")
        return max(max(l1,r1) + max(l2, r2), m1, m2)