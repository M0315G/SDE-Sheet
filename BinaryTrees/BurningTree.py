# Question:
# Given a binary tree and a node data called target. Find the minimum time required to burn the complete
# binary tree if the target is set on fire. It is known that in 1 second all nodes connected to a given node get burned.
# That is its left child, right child, and parent.
# Note: The tree contains unique values.

# Logic:
# we use the same logic as done in All Nodes at Distance K from a target node, create the parent map and traverse radially outwards.
# Just 1 change here would be to keep a flag to see if we're actually traversing any new nodes, bcos if yes then only we increase the count += 1

class Solution:
    def traverse(self, root, parents: dict, target: int):
        node = None
        st = []
        st.append(root)
        while len(st)!=0:
            curr = st.pop(0)
            if curr.data == target:
                node = curr
            if curr.left:
                parents[curr.left.data] = curr
                st.append(curr.left)
            if curr.right:
                parents[curr.right.data] = curr
                st.append(curr.right)
        return node
        

    def minTime(self, root,target):
        parents = {}
        startNode = self.traverse(root, parents, target)
        
        curr = 0
        st = []
        visited = []
        st.append(startNode)
        visited.append(startNode.data)
        while len(st)!=0:
            n = len(st)
            flag = 0
            # print(visited)
            for _ in range(n):
                j = st.pop(0)
                # print(f"For node: {j.data}")
                # Traversing the children
                if j.left and j.left.data not in visited:
                    st.append(j.left)
                    flag = 1
                    # print(f"Left child is: {j.left.data}")
                    visited.append(j.left.data)
                if j.right and j.right.data not in visited:
                    st.append(j.right)
                    flag = 1
                    # print(f"Right child is: {j.right.data}")
                    visited.append(j.right.data)
                # Traversing the parents
                if parents.get(j.data, None) and parents[j.data].data not in visited:
                    # print(f"Parent is: {parents[j.data].data}")
                    st.append(parents[j.data])
                    flag = 1
                    visited.append(parents[j.data].data)
            if flag:
                curr += 1
            
        return curr