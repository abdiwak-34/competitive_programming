class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = ''
        for i in range(len(s)):
            if st and s[i] == st[-1]:
                st = st[:-1]
            else:
                st += s[i]
        return st