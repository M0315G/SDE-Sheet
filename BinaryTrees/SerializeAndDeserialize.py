# Question:
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a
# file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization
# algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the
# original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this
# format, so please be creative and come up with different approaches yourself.

# Logic:
# Choose any one form of serialization i.e. traversal to return as a string and then construct the binary tree from that traversal


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ""
        st = [root]
        while len(st)!=0:
            n = len(st)
            for i in range(n):
                curr = st.pop(0)
                if not curr:
                    s += "#,"
                    continue
                s += str(curr.val) + ","
                st.append(curr.left)
                st.append(curr.right)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == "#":
            return
        lst = data.split(",")
        root = TreeNode(val=int(lst[0]))
        st = [root]
        index = 1
        x = len(lst)
        while len(st) != 0:
            n = len(st)
            for i in range(n):
                curr = st.pop(0)
                if index < x and lst[index] != "#":
                    curr.left = TreeNode(val=lst[index])
                    st.append(curr.left)
                index += 1
                if index < x and lst[index] != "#":
                    curr.right = TreeNode(val=lst[index])
                    st.append(curr.right)
                index += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))