from typing import Optional
# Question
# Given a binary tree having n nodes. Check whether all of its nodes have a value equal to the sum of their child nodes.
# Return 1 if all the nodes in the tree satisfy the given properties, else it returns 0. For every node, the data
# value must be equal to the sum of the data values in the left and right children. Consider the data value 0 for a NULL child.
# Also, leaves are considered to follow the property.

# Logic:
# Do a basic recursion and check this for all nodes.

class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isSum(self, node):
        if not node.left and not node.right:
            return 1
        
        currSum = 0
        answer = 1
        if node.left:
            currSum += node.left.data
            answer = answer and self.isSum(node.left)
        if node.right:
            currSum += node.right.data
            answer = answer and self.isSum(node.right)
        if currSum != node.data:
            return 0
        
        return answer
        
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        return self.isSum(root)


# Another variation is to convert the given BT into a BT which follows this property:

class Solution:
    def reorder(self, node: Optional[Node]):
        if not node:
            return
    
        currSum = 0
        if node.left:
            currSum += node.left.data
        if node.right:
            currSum += node.right.data
        
        if currSum >= node.data:
            node.data = currSum
        else:
            if node.left:
                node.left.data = currSum
            if node.right:
                node.right.data = currSum
        
        self.reorder(node.left)
        self.reorder(node.right)
    
        tot = 0
        if node.left:
            tot += node.left.data
        if node.right:
            tot += node.right.data
        if node.left or node.right:
            node.data = tot
    
    def makeSumProperty(self, root):
        # code here
        return self.reorder(root)