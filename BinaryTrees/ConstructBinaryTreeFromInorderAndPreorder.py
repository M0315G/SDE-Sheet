from typing import List, Optional

# Question:
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is
# the inorder traversal of the same tree, construct and return the binary tree.

# Logic:
# We use a recusive solution, see the video here: https://www.youtube.com/watch?v=aZNaLrVebKQ

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        if preStart > preEnd or inStart > inEnd:
            return
        
        # print(preorder[preStart: preEnd+1], inorder[inStart: inEnd+1])
        # print(f"Rott is: {preorder[preStart]}")
        root = TreeNode(val=preorder[preStart])

        rootIndex = inMap[root.val]
        leftIndex = rootIndex - inStart

        root.left = self.build(preorder, preStart + 1, preStart + leftIndex, inorder, inStart, rootIndex-1, inMap)
        root.right = self.build(preorder, preStart + leftIndex + 1, preEnd, inorder, rootIndex+1, inEnd, inMap)
    
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)