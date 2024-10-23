class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        coS = Counter(s)
        coT = Counter(t)
        if len(s) != len(t):
            return False
        for i in s:
            if coS[i] != coT[i]:
                return False
        return True