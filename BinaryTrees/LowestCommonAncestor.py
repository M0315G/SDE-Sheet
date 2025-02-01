# Question:
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# Logic:
# We build upon the RootToNode.py logic and this time if we encounter a node == p or node==q, we return that node, else null.
# Thus there will be a parent for which both left and right will return a node, thus that parent is our LCA.
# We carry that parent till the top by returning it.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findLCA(self, node, p, q):
        if not node or node == p or node == q:
            if not node:
                return node
            return node

        l = self.findLCA(node.left, p, q)
        r = self.findLCA(node.right, p, q)

        if not l:
            return r
        elif not r:
            return l
        else:
            return node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.findLCA(root, p, q)