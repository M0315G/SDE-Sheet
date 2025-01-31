from typing import List, Optional

# Question
# The boundary of a binary tree is the concatenation of the root,
# the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.
# See full question: https://leetcode.com/problems/boundary-of-binary-tree/description/

# Logic:
# We break it down into 3 parts:
# 1. traversal all the left boundary i.e. start form the root and keep going left until you can, when you cannot go right and keep going until you hit a leaf node.
# 2. Next, we do an in-order traversal but only add the left nodes to the array
# 3. Next, we do the point1 again but this time go all right and then left until leaf node is found.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isLeaf(self, node):
        if not node.left and not node.right:
            return True
        return False
    
    def leftTraversal(self, node, ans):
        curr = node.left
        while curr:
            if not self.isLeaf(curr):
                ans.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    
    def leafTraversal(self, node, ans):
        if self.isLeaf(node):
            ans.append(node.val)
            return
        
        if node.left:
            self.leafTraversal(node.left, ans)
        if node.right:
            self.leafTraversal(node.right, ans)
    
    def rightTraversal(self, node, ans):
        tmp = []
        curr = node.right
        while curr:
            if not self.isLeaf(curr):
                tmp.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        
        for x in range(len(tmp)-1, -1, -1):
            ans.append(tmp[x])

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return answer
        if not self.isLeaf(root):
            answer.append(root.val)
        self.leftTraversal(root, answer)
        self.leafTraversal(root, answer)
        self.rightTraversal(root, answer)  
        return answer    