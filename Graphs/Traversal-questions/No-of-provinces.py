# Question:
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is
# connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
# and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# Logic:
# We iterate over all the vertices and do dfs traversal, ideally all connected vertices will be traversed at once, so the no of time we call
# the traversal code is our count.

from typing import List

class Solution:
    def do_dfs(self, isConnected, visited, node):
        visited[node] = True
        for col in range(len(isConnected)):
            if isConnected[node][col] == 1 and not visited[col]:
                self.do_dfs(isConnected, visited, col)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*(n+1)
        count = 0
        for idx in range(n):
            if not visited[idx]:
                count += 1
                self.do_dfs(isConnected, visited, idx)
        return count
