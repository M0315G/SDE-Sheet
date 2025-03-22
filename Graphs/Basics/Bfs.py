# Question
# Given a undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices
# connected to vertex i. Perform a Breadth First Traversal (BFS) starting from vertex 0, visiting vertices from left to right according to the
# adjacency list, and return a list containing the BFS traversal of the graph.
# Note: Do traverse in the same order as they are in the adjacency list.

# Logic:
# Similar to level order traversal for Binary Trees.

from typing import List
from queue import Queue

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        # code here
        n = len(adj)
        visited = [0]*(n)
        visited[0] = 1
        bfs = []
        q = Queue()
        q.put(0)
        while not q.empty():
            curr = q.get()
            # del queue[-1]
            bfs.append(curr)
            for node in adj[curr]:
                if visited[node] != 1:
                    q.put(node)
        return bfs