class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(pile):
            count = 0
            if pile == 0:
                return True
            for piles in candies:
                count += (piles//pile)
            return count >= k
        left, right = 0, max(candies)
        best = 0
        while left <= right:
            mid = (left+right)//2
            if possible(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best
