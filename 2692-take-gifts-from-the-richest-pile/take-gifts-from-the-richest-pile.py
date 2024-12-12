from math import floor, sqrt
from heapq import heapify, heappop, heappush
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapify(max_heap)
        for i in range(k):
            richest = -heappop(max_heap)
            new = floor(sqrt(richest))
            heappush(max_heap, -new)
        return -sum(max_heap)