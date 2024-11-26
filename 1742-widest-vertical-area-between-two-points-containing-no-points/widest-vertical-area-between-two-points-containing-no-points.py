class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        widest = left = 0
        n = len(points)
        print(points)
        for right in range(1,n):
            widest = max(widest, points[right][0] - points[right-1][0])
        return widest