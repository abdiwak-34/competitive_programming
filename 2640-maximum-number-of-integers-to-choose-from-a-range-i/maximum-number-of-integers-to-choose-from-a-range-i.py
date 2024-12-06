from bisect import bisect_left
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        perm = []
        for i in range(1,n+1):
            if perm and i not in ban:
                perm.append(perm[-1]+i)
            elif i not in ban:
                perm.append(i)
        ans = bisect_left(perm,maxSum+1)
        return ans