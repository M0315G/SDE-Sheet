from typing import List, Optional
# Question:
# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the
# values of all nodes that have a distance k from the target node.
# You can return the answer in any order.

# Logic:
# We construct the parent map to help us with this approach. Use any traversal technique to do so.
# Next, we start at the target node and start going radially outwards upto k steps.
# Meanwhile we keep a visited list to make sure we do not come back to the same nodes again

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, node: Optional[TreeNode], parents: dict):        
        if node.left:
            parents[node.left.val] = node
            self.inorder(node.left, parents)
        if node.right:
            parents[node.right.val] = node
            self.inorder(node.right, parents)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        self.inorder(root, parents)
        # print(parents)
        curr = 0
        st = []
        visited = []
        st.append(target)
        visited.append(target.val)
        while len(st)!=0:
            n = len(st)
            if curr == k:
                break
            curr += 1
            print(visited)
            for _ in range(n):
                j = st.pop(0)
                # print(f"For node: {j.val}")
                # Traversing the children
                if j.left and j.left.val not in visited:
                    st.append(j.left)
                    # print(f"Left child is: {j.left.val}")
                    visited.append(j.left.val)
                if j.right and j.right.val not in visited:
                    st.append(j.right)
                    # print(f"Right child is: {j.right.val}")
                    visited.append(j.right.val)
                # Traversing the parents
                if parents.get(j.val, None) and parents[j.val].val not in visited:
                    # print(f"Parent is: {parents[j.val].val}")
                    st.append(parents[j.val])
                    visited.append(parents[j.val].val)
                # print(st)
        ans = []
        for k in st:
            ans.append(k.val)
        return ans