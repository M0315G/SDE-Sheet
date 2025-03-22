# Question:
# Given an integer n representing number of vertices. Find out how many undirected graphs
# (not necessarily connected) can be constructed out of a given n number of vertices.

# Logic:
MOD = int(1e9 + 7)

class Solution:
    def count(self, n):
        x = (n *( n - 1 )) //2
        return (pow(2, x)) # or pow(2, x, MOD) if MOD is to be used   