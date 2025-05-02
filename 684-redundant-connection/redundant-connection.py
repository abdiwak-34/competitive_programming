class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size+2)]
        self.rank = [0] * (size+2)
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            if self.rank[rx] > self.rank[ry]:
                self.parent[ry] = rx
            elif self.rank[ry] > self.rank[rx]:
                self.parent[rx] = ry
            else:
                self.parent[ry] = rx
                self.rank[rx] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        Tree = UnionFind(len(edges))
        for a, b in edges:
            if Tree.connected(a,b):
                return [a,b]
            else:
                Tree.union(a,b)
