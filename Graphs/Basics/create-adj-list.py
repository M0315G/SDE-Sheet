# Question:
# Given an undirected graph with V nodes and E edges, create and return an adjacency list of the graph. 0-based indexing is followed everywhere.

# Logic:
from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        adj = [[] for _ in range(V+1)]
        # print(adj)
        for a, b in edges:
            # print(a, b)
            adj[a].append(b)
            # print(adj)
            adj[b].append(a)
            # print(adj)
        return adj