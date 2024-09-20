
def topological_sort(n):
    graph = {}
    edges = [[],[],[3],[1],[0,1],[2,0]]
    lst = []
    for i in range(n):
        graph[i] = edges[i]

    visited = []
    for i in range(n):
        visited.append(0)
    print(graph)
    def dfs(node):
        visited[node] = 1
        for j in graph[node]:
            if visited[j] == 0:
                dfs(j)
        lst.append(node)

    for i in range(0,n):
        if visited[i] == 0:
                dfs(i)

    print(lst[::-1])
topological_sort(6)

