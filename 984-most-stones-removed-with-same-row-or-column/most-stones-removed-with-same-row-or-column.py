class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def removeStones(self, stones):
        component = UnionFind()
        
        for x, y in stones:
            component.union(x, y + 10001)
        return len(stones) - len({component.find(x) for x, y in stones})
