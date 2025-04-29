from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for wieght in stones:
            heappush(heap, -wieght)
        
        while len(heap) > 1:
            x = -heappop(heap)
            y = -heappop(heap)
            if x > y:
                heappush(heap, -(x-y))
            if y > x:
                heappush(heap, -(y-x))
        if not heap:
            return 0
        return -heappop(heap)
        