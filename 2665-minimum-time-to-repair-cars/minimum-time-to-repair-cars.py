class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepair(time):
            no_cars = 0
            for r in ranks:
                no_cars += int(sqrt(time/r))
            return no_cars >= cars
        
        left, right = 0, (cars**2) * max(ranks)
        best = right
        while left <= right:
            mid = (left+right)//2

            if canRepair(mid):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        return best