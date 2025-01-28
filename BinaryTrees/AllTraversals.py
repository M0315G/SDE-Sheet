from sys import *
from collections import *
from math import *

# Question:
# You have been given a Binary Tree of 'N' nodes, where the nodes have integer values.
# Your task is to return the ln-Order, Pre-Order, and Post-Order traversals of the given binary tree.

# Logic: We use 1, 2, 3 values to denote the traversals.

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    st = []
    st.append([root, 1])
    preorder, inorder, postorder = [], [], []
    while len(st) != 0:
        ele = st.pop(-1)
        if ele[1] == 1:
            preorder.append(ele[0].data)
            st.append([ele[0], 2])
            if ele[0].left:
                st.append([ele[0].left, 1])
        elif ele[1] == 2:
            inorder.append(ele[0].data)
            st.append([ele[0], 3])
            if ele[0].right:
                st.append([ele[0].right, 1])
        elif ele[1] == 3:
            postorder.append(ele[0].data)
    
    return inorder, preorder, postorder
