# Question:
# Given a binary tree, convert the binary tree to its Mirror tree.
# Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.

# Logic:
# Do level order traversal and just swap left and right each time.

class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None

# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        st = [root]
        while len(st)!=0:
            n = len(st)
            for i in range(n):
                curr = st.pop(0)
                curr.left, curr.right = curr.right, curr.left
                if curr.left:
                    st.append(curr.left)
                if curr.right:
                    st.append(curr.right)
        return root