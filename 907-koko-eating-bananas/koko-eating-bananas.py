class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(perhour):
            hours = 0
            for p in piles:
                hours += math.ceil(p/perhour)
            return hours <= h
        
        left, right = 1, max(piles)
        best = right
        while left <= right:
            mid = (left+right)//2
            if possible(mid):
                best = mid
                right = mid -1
            else:
                left = mid +1
        return best