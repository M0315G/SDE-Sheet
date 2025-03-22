# Question:
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all
# four edges of the grid are all surrounded by water.

# Logic:
# We consider each cell in the grid as node and the condition of being conencted is that it should be in either of the 4 directions: up, down, left, right

from collections import deque
from typing import List

class Solution:
    def bfs(self, grid, visited, a, b, m, n):
        visited[a][b] = True
        q = deque()
        q.append([a, b])
        while q:
            i, j = q.popleft()
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for dr, dc in directions:
                r, c = i + dr, j + dc
                if 0 <= r < m and 0 <= c < n and grid[r][c] == "1" and not visited[r][c]:
                    q.append([r, c])
                    visited[r][c] = True

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    islands += 1
                    self.bfs(grid, visited, i, j, m, n)
        return islands

