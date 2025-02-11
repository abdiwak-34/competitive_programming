class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        ans = []
        order = defaultdict(list)
        for i in range(n):
            for j in range(m):
                order[i+j].append(mat[i][j])
       
        for i in range(n+m-1):
            if i % 2 == 0:
                ans.extend(reversed(order[i]))
            else:
                ans.extend(order[i])
        return ans