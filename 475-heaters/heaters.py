class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0

        for house in houses:
            i = bisect_left(heaters, house)

            left = heaters[i - 1] if i > 0 else float('-inf')
            right = heaters[i] if i < len(heaters) else float('inf')

            dist = min(abs(house - left), abs(house - right))
            res = max(res, dist)

        return res
