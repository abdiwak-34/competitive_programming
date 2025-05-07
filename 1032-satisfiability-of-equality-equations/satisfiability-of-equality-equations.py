class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(int)
        
    def find(self, x):
        if x not in self.parent:
            return x
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
        return self.find(x) == self.find(x)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        Equation = UnionFind()
        for equa in equations:
            if equa[1:3] == '==':
                Equation.union(equa[0], equa[3])
        
        for equa in equations:
            if equa[1:3] == '!=' and Equation.find(equa[0]) == Equation.find(equa[3]):
                return False
        
        return True
