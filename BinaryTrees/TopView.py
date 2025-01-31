# Question:
# You are given a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible
# when the tree is viewed from the top.
# Note: 
# --> Return the nodes from the leftmost node to the rightmost node.
# --> If two nodes are at the same position (horizontal distance) and are outside the shadow of the tree, consider the leftmost node only. 

# Logic:
# Use the same traversal technique as did in Vertical order but this time we only store the 1st node we encounter for each vertical level.
# Finally sort it and send the answer

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        data = {}
        st = []
        st.append([0, 0, root])
        while len(st)!=0:
            n = len(st)
            for i in range(n):
                x, y, node = st.pop(0)
                if not data.get(x, None):
                    data[x] = node.data
                if node.left:
                    st.append([x-1, y+1, node.left])
                if node.right:
                    st.append([x+1, y+1, node.right])

        answer = []
        for _key in sorted(data.keys()):
            answer.append(data[_key])
        return answer