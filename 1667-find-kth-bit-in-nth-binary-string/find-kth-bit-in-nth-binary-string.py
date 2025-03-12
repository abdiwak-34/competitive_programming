class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ['0']
        def recur(s,n):
            if n == 0:
                return
            l = len(s)-1
            s.append('1')
            while l >= 0:
                s.append('1' if s[l] == '0' else '0')
                l-= 1
            n -= 1
            recur(s,n)
        recur(s,n-1)
        return s[k-1]