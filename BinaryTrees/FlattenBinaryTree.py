from typing import Optional
# Question:
# Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# logic:
# To replace in place we use a simple rule:
# append the left subtree of the current node to it's right and then iterate till the right most end of this subtree to append the original
# right subtree of the current node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rearrange(self, node: Optional[TreeNode]):
        if not node:
            return

        temp = None
        if node.left:
            temp = node.right
            node.right = node.left
            node.left = None
            curr = node
            while curr.right:
                curr = curr.right
            curr.right = temp
        self.rearrange(node.right)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.rearrange(root)
        