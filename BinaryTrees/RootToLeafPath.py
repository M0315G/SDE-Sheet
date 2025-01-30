# Question:
# Given a Binary Tree, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.
# Note: The paths should be returned such that paths from the left subtree of any node are listed first, followed by paths from the right subtree.

# Logic:
# Idea is to recusively traverse the tree in pre-order traversal and whenever we reach a leaf node, we return it's value in a list:
# [leaf] and we get similar lists from left and right recursively and we keep on adding the current node to the mix.

class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

class Solution:
    def findPaths(self, node):
        if not node:
            return -1
        
        # print(f"For node: {node.data}")
        answer = []
        left = self.findPaths(node.left)
        if left != -1:
            for l in left:
                l.append(node.data)
                answer.append(l)
        # print(f"After left we got: {answer}, {left} ")
        right = self.findPaths(node.right)
        if right != -1:
            for r in right:
                r.append(node.data)
                answer.append(r)
        if right == -1 and left == -1:
            answer.append([node.data])
        # print(f"After right we got: {answer}, {right}")
        return answer
        
    def Paths(self, root):
        # code here
        ans = []
        answer = self.findPaths(root)
        for x in answer:
            ans.append(x[::-1])
        return ans