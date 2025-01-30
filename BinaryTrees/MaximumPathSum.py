from typing import Optional

# Question:
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
# A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Logic:
# It's similar to the max height, we calculate the max value possible in left and right subtree but we cap the values at 0, we don't want -ve values
# and finally update the global maxVal if currMax is greater.

# Check the case to understand more:
# [9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]
# Here in the root node of 2 which has child -6 and -6, since both of them give -ve, the value we returned was got
# by max(node.val + max(0, 0), node.val + max(left, right)) --> considering both left and right were -ve so they turned out to be 0.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSum(self, node: Optional[TreeNode], maxVal: list):
        if not node:
            return 0
        left = max(0, self.maxSum(node.left, maxVal))
        right = max(0, self.maxSum(node.right, maxVal))
        
        currMax = left + right + node.val
        # print(f"At node: {node.val} the currMax is: {currMax}")
        # print(f"Left is: {node.left.val if node.left else 0000} with maxval as: {left}")
        # print(f"Right is: {node.right.val if node.right else 0000} with maxval as: {right}")
        if currMax > maxVal[0]:
            maxVal[0] = currMax
        return node.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = [float("-inf")]
        self.maxSum(root, maxVal)
        return maxVal[0]