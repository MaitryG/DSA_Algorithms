class DisjointSet:
    rank = []
    parent = []
    size = []
    def __init__(self, n):
        for i in range(n):
            self.rank.append(0)
            self.parent.append(i)
            self.size.append(1)
            print(self.parent)

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

ds = DisjointSet(8)
print(ds.parent)
# ds.union_by_rank(1, 2)
# ds.union_by_rank(2, 3)
# ds.union_by_rank(4, 5)
# ds.union_by_rank(6, 7)
# ds.union_by_rank(5, 6)
#
# if ds.find_ult_parent(3) == ds.find_ult_parent(7):
#     print("Same component")
# else:
#     print("Not same component")
#
# ds.union_by_rank(3, 7)
#
# if ds.find_ult_parent(3) == ds.find_ult_parent(7):
#     print("Same component")
# else:
#     print("Not same component")

ds.union_by_size(1, 2)
ds.union_by_size(2, 3)
ds.union_by_size(4, 5)
ds.union_by_size(6, 7 )
ds.union_by_size(5, 6)

if ds.find_ult_parent(3) == ds.find_ult_parent(7):
    print("Same component")
else:
    print("Not same component")

ds.union_by_rank(3, 7)

if ds.find_ult_parent(3) == ds.find_ult_parent(7):
    print("Same component")
else:
    print("Not same component")
