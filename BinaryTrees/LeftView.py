# Question:
# You are given the root of a binary tree. Your task is to return the left view of the binary tree.
# The left view of a binary tree is the set of nodes visible when the tree is viewed from the left side.
# If the tree is empty, return an empty list.

# Logic:
# We use the logic that for each level of the tree only 1 node should be printed and that should be the left most one.
# Thus we maintain a level key with each node and traverse the tree in preorder traversal, whenever we get a level which has not been printed, we
# add it to the answer.

class Solution:
    def LeftView(self, root):
        # code here
        if not root:
            return []
        st = []
        level = 1
        st.append([root, level])
        answer = []
        maxLevel = 0
        while len(st)!=0:
            ele = st.pop(-1)
            # print(f"Curr is: {ele[0].data} with level: {ele[1]}")
            if ele[1] > maxLevel:
                answer.append(ele[0].data)
                maxLevel = ele[1]
            
            level = ele[1]
            if ele[0].right or ele[0].left:
                level += 1
            
            if ele[0].right:
                st.append([ele[0].right, level])
            if ele[0].left:
                st.append([ele[0].left, level])
        
        return answer