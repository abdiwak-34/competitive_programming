class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

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

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        def index(i, j):
            return i * n + j

        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n
        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0),
        }

        streets = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }

        for i in range(m):
            for j in range(n):
                for dx, dy in streets[grid[i][j]]:
                    ni, nj = i + dx, j + dy
                    if inbound(ni, nj) and opposite[(dx, dy)] in streets[grid[ni][nj]]:
                        uf.union(index(i, j), index(ni, nj))

        return uf.find(index(0, 0)) == uf.find(index(m - 1, n - 1))
