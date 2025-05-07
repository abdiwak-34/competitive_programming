class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
		
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        
        if ry != rx:
            if self.rank[rx] > self.rank[ry]:
                self.parent[ry] = rx
            elif self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
            else:
                self.parent[rx] = ry
                self.rank[ry] += 1
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        Point = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                xdist = abs(points[i][0] - points[j][0])
                ydist = abs(points[i][1] - points[j][1])
                edges.append((xdist+ydist, i, j))

        edges.sort()
        total = 0
        count = 0
        for edge in edges:
            w, u, v = edge
            if not Point.connected(u, v):
                Point.union(u,v)
                count += 1
                total += w
                if count == n-1:
                    break
        return total