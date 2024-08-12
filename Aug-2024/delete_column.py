class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        for i in range(len(strs[0])):
            now = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] > now:
                    return i
                now = strs[j][i]
        return 0
