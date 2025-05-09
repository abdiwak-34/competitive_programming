class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
		
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        
        if ry != rx:
            if rx < ry:
                self.parent[ry] = rx
            else:
                self.parent[rx] = ry

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        for a, b in zip(s1, s2):
            uf.union(ord(a) - 97, ord(b) - 97)
        ans = []
        for c in baseStr:
            small = uf.find(ord(c) - 97)
            ans.append(chr(small + 97))
        return ''.join(ans)
