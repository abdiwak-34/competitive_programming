class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        perm = []
        for i in range(1,n+1):
            if i not in ban:
                perm.append(i)
        ans = ptr = 0
        while ptr < len(perm):
            if ans + perm[ptr] > maxSum:
                return ptr
            ans += perm[ptr]
            ptr += 1
        return ptr