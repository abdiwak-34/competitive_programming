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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        e_name = {}

        for account in accounts:
            name = account[0]
            f_email = account[1]
            for email in account[1:]:
                uf.union(f_email, email)
                e_name[email] = name

        roots = defaultdict(list)
        for email in e_name:
            root = uf.find(email)
            roots[root].append(email)

        res = []
        for r_email, emails in roots.items():
            res.append([e_name[r_email]] + sorted(emails))
        return res
