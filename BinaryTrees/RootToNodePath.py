# Question:
# Give a binary tree and a target node, find the path of the root to that target node.

# Logic:
# We recursively do in-order traversal and check if the current node == target, if yes, we return True
# Else return false
# In each iteration the curr node that is being tested is added to the array, if it's == target then return True else we pop it

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

class Solution:
    def findPath(self, node, target, currPath):
        if not node:
            return False
        
        currPath.append(node.data)
        if node.data == target:
            return True

        if self.findPath(node.left, target, currPath) or self.findPath(node.right, target, currPath):
            return True
        
        currPath.pop(-1)
        return False
        
    def Path(self, root):
        # code here
        ans = []
        ans.append(root.data)
        self.findPath(root, ans)
        return ans