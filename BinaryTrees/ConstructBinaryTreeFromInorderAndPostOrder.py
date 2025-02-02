from typing import List, Optional

# Question:
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is
# the postorder traversal of the same tree, construct and return the binary tree.

# Logic:
# We build upon the solution in using Preorder and Inorder, see the video here: https://www.youtube.com/watch?v=LgLRTaEMRVc

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def build(self, postorder, posStart, posEnd, inorder, inStart, inEnd, inMap):
        if posStart > posEnd or inStart > inEnd:
            return
        
        # print(postorder[posStart: posEnd+1], inorder[inStart: inEnd+1])
        # print(f"Rott is: {preorder[posEnd]}")
        root = TreeNode(val=postorder[posEnd])

        rootIndex = inMap[root.val]
        leftIndex = rootIndex - inStart

        root.left = self.build(postorder, posStart, posStart + leftIndex - 1, inorder, inStart, rootIndex-1, inMap)
        root.right = self.build(postorder, posStart + leftIndex, posEnd - 1, inorder, rootIndex+1, inEnd, inMap)
    
        return root
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i
        return self.build(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1, inMap)
