# Question:
# Given a connected undirected graph represented by an adjacency list adj, which is a vector of vectors where each
# adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Traversal (DFS) starting from vertex 0,
# visiting vertices from left to right as per the adjacency list, and return a list containing the DFS traversal of the graph.
# Note: Do traverse in the same order as they are in the adjacency list.

# Logic:
# Use recrusion to traverse in depth.

class Solution:
    def do_dfs(self, adj, vis, dfs, node):
        vis[node] = 1
        dfs.append(node)
        
        for n in adj[node]:
            if vis[n] != 1:
                self.do_dfs(adj, vis, dfs, n)
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        n = len(adj)
        vis = [0]*n
        dfs = []
        self.do_dfs(adj, vis, dfs, 0)
        return dfs