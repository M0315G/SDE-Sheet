# Question:
# Given a binary tree, return an array where elements represent the bottom view of the binary tree from left to right.
# Note: If there are multiple bottom-most nodes for a horizontal distance from the root,
# then the latter one in the level traversal is considered i.e the right one.

# Logic:
# We use the same logic as in Top View of a BT but this time we store the 1st node we encounter and then for every next node of same vertical level:
#      --> we check if the current node's tree level is >= the node stored, if yes then replace.
# Finally sort it and send the answer

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def bottomView(self, root):
        data = {}
        st = []
        st.append([0, 0, root])
        while len(st)!=0:
            n = len(st)
            for i in range(n):
                x, y, node = st.pop(0)
                if not data.get(x, None):
                    data[x] = [y, node.data]
                else:
                    if data[x][0] <= y:
                        data[x] = [y, node.data]
                if node.left:
                    st.append([x-1, y+1, node.left])
                if node.right:
                    st.append([x+1, y+1, node.right])

        answer = []
        for _key in sorted(data.keys()):
            answer.append(data[_key][1])
        return answer