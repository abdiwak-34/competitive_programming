class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = tt = ''
        for i in range(len(s)):
            if s[i] == '#':
                st = st[:-1]
            else:
                st += s[i]
        for i in range(len(t)):
            if t[i] == '#':
                tt = tt[:-1]
            else:
                tt += t[i]
        return st == tt