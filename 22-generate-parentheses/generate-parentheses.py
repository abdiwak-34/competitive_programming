class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def find(parr,open_p,close_p):
            if close_p == n:
                ans.append(''.join(parr[:]))
                return
            if open_p < n:
                parr.append('(')
                find(parr, open_p+1,close_p)
                parr.pop()
            if close_p < open_p:
                parr.append(')')
                find(parr, open_p,close_p+1)
                parr.pop()
        find(['('],1,0)
        return ans