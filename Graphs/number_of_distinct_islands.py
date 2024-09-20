# User function Template for python3

import sys
from typing import List

sys.setrecursionlimit(10 ** 8)


class Solution:
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        # code here
        def dfs(i, j, grid, lst, row0, col0):
            visited[i][j] = 1
            lst.append([i - row0, j - col0])
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in directions:
                r = i + dr
                c = j + dc
                if 0 <= r < m and 0 <= c < n and visited[r][c] == 0 and grid[r][c] == 1:
                    dfs(r, c, grid, lst, i, j)

        m = len(grid)
        n = len(grid[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        print(visited)
        # for a in range(m):
        #     for b in range(n):
        #         visited[a][b] = 0
        # print(visited)
        res = []
        for i in range(m):
            for j in range(n):
                print(i, j)
                if visited[i][j] == 0 and grid[i][j] == 1:
                    lst = []
                    dfs(i, j, grid, lst, i, j)
                    if lst not in res:
                        res.append(lst)
        print(res)
        return len(res)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

    obj = Solution()
    print(obj.countDistinctIslands(grid))
# } Driver Code Ends
# 4 5
# 1 1 0 0 0
# 1 1 0 0 0
# 0 0 0 1 1
# 0 0 0 1 1