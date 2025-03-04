class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev_end = points[0][1]
        count = 1
        for point in points:
            if point[0] > prev_end:
                count += 1
                prev_end = point[1]
            prev_end = min(prev_end, point[1])
        return count