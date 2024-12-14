class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            hour = 0
            if k == 0:
                return False
            for pile in piles:
                hour += math.ceil(pile/k)
                if hour > h:
                    return False
            return True
        left = 0 
        right = min_k = sum(piles)
        while left <= right:
            mid = (left + right) // 2
            if possible(mid):
                min_k = min(min_k, mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_k