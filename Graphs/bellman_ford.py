from typing import List
import heapq
class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def bellman_ford(self, V: int, adj: List[List[int]], S: int) -> List[int]:
        n = V
        dist = [float('inf') for i in range(n)]
        dist[S] = 0

        for i in range(V-1):
            for j in adj:
                u = j[0]
                v = j[1]
                w = j[2]
                if dist[u]!=float('inf') and dist[u]+w<dist[v]:
                    dist[v] = dist[u]+w
        return dist

# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    V, E = 3, 3
    adj = [[] for i in range(V)]
    lst = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
    for i in lst:
        u = i[0]
        v = i[1]
        w = i[2]
        adj[u].append([v,w])

    S = 2 # source
    ob = Solution()
    # print(adj)
    res = ob.bellman_ford(V, lst, S)
    for i in res:
        print(i, end=" ")
    print()

# } Driver Code Ends