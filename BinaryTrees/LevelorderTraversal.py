from typing import List, Optional

# Question:
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Logic:
# Put the current level nodes in a stack and then pop each one out one by one.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        queue = []
        if not root:
            return []
        queue.append(root)
        while len(queue) != 0:
            currLevel = []
            n = len(queue)
            for i in range(n):
                print(i)
                ele = queue[0]
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                currLevel.append(ele.val)
                queue.pop(0)
            answer.append(currLevel)
        return answer
        