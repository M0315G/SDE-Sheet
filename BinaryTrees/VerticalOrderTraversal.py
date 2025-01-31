from typing import List, Optional
from collections import defaultdict

# Question:
# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
# See question here: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

# Logic:
# Basic idea is to treat the tree as a 2d coordinate system with root being at (0, 0)
# When we move to left, the x values goes -1 and +1 when we go to the right
# y values always +1 when moving from root to children.
# Construct a dictonary of dictonary in this way and then add it in the final list of list maintaining the sorted order.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        data = defaultdict(dict)
        st = []
        st.append([0, 0, root])
        while len(st)!=0:
            n = len(st)
            for i in range(n):
                # x represents the vertical level, y represents the tree level 
                x, y, node  = st.pop(0)
                if not data[x].get(y, None):
                    data[x][y] = [node.val]
                else:
                    data[x][y].append(node.val)
                if node.left:
                    st.append([x-1, y+1, node.left])
                if node.right:
                    st.append([x+1, y+1, node.right])
        
        answer = []
        for level in sorted(data.keys()):
            ans = []
            level_data = data[level]
            for level, vals in level_data.items():
                ans.extend(sorted(vals))
            answer.append(ans)
        return answer
        