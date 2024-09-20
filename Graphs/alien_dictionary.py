def check(s1, s2):
    p = 0
    n = min(len(s1), len(s2))
    while p < n:
        if s1[p] != s2[p]:
            return [s1[p], s2[p]]
        p+=1
    return []


if __name__=='__main__':
    strings = ['baa','abcd','abca','cab','cad']
    graph = {}
    for i in range(0,26):
        graph[i] = []

    for i in range(len(strings)-1):
        s1 = strings[i]
        s2 = strings[i+1]

        c = check(s1, s2)
        if c is None:
            continue
        else:
            graph[ord(c[0]) - ord('a')].append(ord(c[1])-ord('a'))

    print(graph)
    lst = []
    def dfs(node):
        visited[node] = 1
        for j in graph[node]:
            if visited[j] == 0:
                dfs(j)
        lst.append(node)


    visited = [0 for i in range(0,26)]
    for i in range(0,26):
        if visited[i] == 0:
            dfs(i)

    print(lst)