class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = []
        for i in range(len(s)):
            ans.append(s[indices.index(i)])
        return ''.join(ans)