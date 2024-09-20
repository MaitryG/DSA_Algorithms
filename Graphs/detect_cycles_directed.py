def detect_cycles_directed(n):
    graph = {}
    edges = [[0,1],[1,2],[2,3],[3,4],[3,7],[4,5],[5,6],[8,2],[8,9],[9,10],[10,8]]
    for i in range(n):
        graph[i] = []

    for j, k in edges:
        graph[j].append(k)
    visited = []
    path_visited = []
    for i in range(n):
        visited.append(0)
        path_visited.append(0)

    def dfs(node, visited, path_visited):
        visited[node] = 1
        path_visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                if dfs(i, visited, path_visited):
                    return True
            else:
                if path_visited[i] == 1:
                    return True
        path_visited[node] = 0
        return False

    for i in range(n):
        if visited[i] == 0:
            if dfs(i, visited, path_visited):
                print("Cycle found")

detect_cycles_directed(12)

