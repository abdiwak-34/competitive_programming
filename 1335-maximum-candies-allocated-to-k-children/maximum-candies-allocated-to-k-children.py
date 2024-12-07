class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(maxpile):
            child = 0
            if maxpile == 0:
                return True
            for pile in candies:
                child += pile // maxpile
            return child >= k
        left, right = 0, max(candies)
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if possible(mid):
                result = max(mid, result)
                left = mid + 1
            else:
                right = mid - 1
        return result
