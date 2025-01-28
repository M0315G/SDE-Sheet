from typing import List, Optional

# Question:
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Logic: Root-Left-Right

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, node, arr):
        if not node:
            return
        arr.append(node.val)
        self.preorder(node.left, arr)
        self.preorder(node.right, arr)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        # Recurisve
        # self.preorder(root, answer)

        # Iterative
        if not root:
            return []
        nodes = []
        nodes.append(root)
        while len(nodes) != 0:
            node = nodes[-1]
            nodes.pop(-1)
            answer.append(node.val)
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)
        return answer