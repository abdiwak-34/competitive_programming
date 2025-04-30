class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                if ladders > 0:
                    heappush(heap, diff)
                    ladders -= 1
                else:
                    heappush(heap, diff)
                    x = heappop(heap)
                    if bricks >= x:
                        bricks -= x
                    else:
                        return i-1
        return len(heights)-1
        