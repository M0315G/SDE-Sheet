from typing import Optional

# Question:
# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
# and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# Design an algorithm that runs in less than O(n) time complexity.

# Logic:
# We check the heights of both left and right subtree. If they're same answer is 2^h -1.
# If not then recurisvely check the same property for it's left and right subtree and the final answer would be:
#   1 + nodes in left subtree + nodes in right subtree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLHeight(self, node: Optional[TreeNode]):
        ht = 0
        while node:
            ht += 1
            node = node.left
        return ht
    
    def findRHeight(self, node: Optional[TreeNode]):
        ht = 0
        while node:
            ht += 1
            node = node.right
        return ht

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lh = self.findLHeight(root)
        rh = self.findRHeight(root)

        if lh == rh:
            return (1<<lh)-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        