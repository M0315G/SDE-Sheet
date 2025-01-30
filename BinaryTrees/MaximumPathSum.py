from typing import Optional

# Question:
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
# A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Logic:
# It's similar to the max height, we calculate the max value possible in left and right subtree and then check all the combinations:
# currMax = max(
#     left + right + node.val, # general case
#     left + node.val, # when right is -ve
#     right + node.val, # when left is -ve
#     node.val, # when both are -ve
# )
# and finally update the global maxVal if currMax is greater. One thing to note is in case of returning the maxVal for each subtree, if both
# left and right are -ve then returning only the value of root node is also valid.

# Check the case to understand more:
# [9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]
# Here in the root node of 2 which has child -6 and -6, since both of them give -ve, the value we returned was got by max(node.val, node.val + max(left, right))

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
        left = self.maxSum(node.left, maxVal)
        right = self.maxSum(node.right, maxVal)

        currMax = max(
            left + right + node.val, # general case
            left + node.val, # when right is -ve
            right + node.val, # when left is -ve
            node.val, # when both are -ve
        )
        # print(f"At node: {node.val} the currMax is: {currMax}")
        # print(f"Left is: {node.left.val if node.left else 0000} with maxval as: {left}")
        # print(f"Right is: {node.right.val if node.right else 0000} with maxval as: {right}")
        # print(f"Combinations: {left + right + node.val}, {left + node.val}, {right + node.val}, {node.val}")

        if currMax > maxVal[0]:
            maxVal[0] = currMax
        return max(node.val + max(left, right), node.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = [float("-inf")]
        val = self.maxSum(root, maxVal)
        if val > maxVal[0]:
            maxVal[0] = val
        return maxVal[0]