from typing import List
import heapq
class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
        n = V
        dist = [float('inf') for i in range(n)]
        dist[S] = 0
        pq = []
        heapq.heappush(pq, [0, S])

        while pq:
            node_lst = heapq.heappop(pq)
            node = node_lst[1]
            dis = node_lst[0]

            for i in adj[node]:
                v = i[0]
                w = i[1]
                if w + dis < dist[v]:
                    dist[v] = w + dis
                    heapq.heappush(pq, [dist[v], v])

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
    lst = [[[1,1],[2,6]],[[2,3],[0,1]],[[1,3],[0,6]]]
    for i in range(V):
        for j in range(len(lst[i])):
            u = i
            v = lst[i][j][0]
            w = lst[i][j][1]

            adj[u].append([v, w])
            adj[v].append([u, w])
    S = 2 # source
    ob = Solution()

    res = ob.dijkstra(V, adj, S)
    for i in res:
        print(i, end=" ")
    print()

# } Driver Code Ends