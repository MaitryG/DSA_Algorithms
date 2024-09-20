def detect_cycles(n):
    graph = {}
    edges = [[0, 1],[2,3],[2,1],[1,3]]
    for i in range(n):
        graph[i] = []

    for j, k in edges:
        graph[j].append(k)
    visited = []
    for i in range(n):
        visited.append(0)

    def dfs(node, parent):
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                if dfs(i, node):
                    return True
            else:
                if i != parent:
                    return True
        return False

    print(dfs(0,-1))
detect_cycles(4)

