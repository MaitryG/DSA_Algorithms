class DisjointSet:
    rank = []
    parent = []
    size = []
    def __init__(self, n):
        for i in range(n):
            self.rank.append(0)
            self.parent.append(i)
            self.size.append(1)

    def find_ult_parent(self, node):
        if node == self.parent[node]:
            return node

        ulp = self.find_ult_parent(self.parent[node])
        self.parent [node] = ulp
        return self.parent[node]

    def union_by_rank(self, u, v):
        ult_u = self.find_ult_parent(u)
        ult_v = self.find_ult_parent(v)
        if ult_u == ult_v:
            return
        if self.rank[ult_v] < self.rank[ult_u]:
            self.parent[ult_v] = ult_u
        elif self.rank[ult_v] > self.rank[ult_u]:
            self.parent[ult_u] = ult_v
        else:
            self.parent[ult_v] = ult_u
            rank_u = self.rank[ult_u]
            self.rank[ult_u] = rank_u + 1

    def union_by_size(self, u, v):
        ult_u = self.find_ult_parent(u)
        ult_v = self.find_ult_parent(v)
        if ult_u == ult_v:
            return
        if self.size[ult_u] < self.size[ult_v]:
            self.parent[ult_u] = ult_v
            self.size[ult_v] += self.size[ult_u]
        else:
            self.parent[ult_v] = ult_u
            self.size[ult_u] += self.size[ult_v]

def isValid(row, col, n, m):
    if 0 <= row < n and 0 <= col < m:
        return True
    return False
if __name__ == "__main__":
    count = 0
    n = 4
    m = 5
    ds = DisjointSet(n*m)
    mat = [[0 for i in range(n)] for j in range(m)] #queries
    print(mat)
    ans = []
    vis = [[0 for i in range(n)] for j in range(m)]

    for i in range(len(mat)):
        row = mat[i][0]
        col = mat[i][1]
        if vis[row][col] == 1:
            ans.append(vis[row][col])
            continue

        vis[row][col] = 1
        count+=1
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for indx in range(4):
            new_row = row + dr
            new_col = col + dc

            if isValid(new_row, new_col, n, m):
                if vis[new_row][new_col] == 1:
                    nodeNum = row * m + col
                    adjNodeNum = new_row * m + new_col
                    if ds.find_ult_parent(nodeNum) != ds.find_ult_parent(adjNodeNum):
                        count -= 1
                        ds.union_by_size(nodeNum, adjNodeNum)