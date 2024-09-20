
if __name__=='__main__':
    n = 7
    edges = [[0,1,2],[1,3,1],[2,3,3],[4,0,3],[4,2,1],[5,4,1],[6,4,2],[6,5,3]]
    graph = {}
    for i in range(n):
        graph[i] = []
    print(graph)
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        w = edges[i][2]
        graph[u].append([v,w])
    visited = [0 for i in range(n)]
    lst = []
    def dfs(node):
        visited[node] = 1
        for j in graph[node]:
            u = j[0]
            if visited[u] == 0:
                dfs(u)
        lst.append(node)

    #Do the topological sort
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
    print(lst)

    #Do the distancing
    dist = [float('inf') for i in range(n)]
    dist[6] = 0 # Source = 6
    while lst:
        node = lst.pop()
        for i in graph[node]:
            v = i[0]
            w = i[1]
            if dist[node] + w < dist[v]:
                dist[v] = dist[node]+w
    print(dist)
