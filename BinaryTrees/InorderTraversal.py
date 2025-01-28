from typing import List, Optional

# Question:
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Logic: Left-Root-Right

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, node, arr):
        if not node:
            return
        self.inorder(node.left, arr)
        arr.append(node.val)
        self.inorder(node.right, arr)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        # Recursive
        # self.inorder(root, answer)

        # Iterative
        if not root:
            return []
        stack = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                curr = stack[-1]
                stack.pop(-1)
                answer.append(curr.val)
                node = curr.right
            
            if len(stack) == 0 and not node:
                break
        return answer