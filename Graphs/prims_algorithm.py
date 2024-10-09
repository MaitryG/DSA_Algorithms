import heapq


def prims(graph):
    pq = []
    heapq.heappush(pq,[0,0])
    visited = [0 for i in range(n)]
    mst = []
    sum1 = 0
    while pq:
        w, node = heapq.heappop(pq)
        if visited[node] == 1:
            continue
        visited[node] = 1
        mst.append(node)
        sum1 += w
        for j in graph[node]:
            w = j[1]
            v = j[0]
            if visited[v] == 0:
                heapq.heappush(pq,[w, v])

    return sum1


if __name__ == '__main__':
    n = 5
    adj = [[] for i in range(n)]
    input = [[0,1,2],[1,2,3],[0,3,6],[3,1,8],[1,4,5],[4,2,7]]
    for i in input:
        u = i[0]
        v = i[1]
        w = i[2]
        adj[u].append([v,w])
        adj[v].append([u,w])
    print(prims(adj))


