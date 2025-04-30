from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key, val in count.items():
            heappush(heap, (val, key))
            if len(heap) > k:
                heappop(heap)
        
        ans = []
        for _, element in heap:
            ans.append(element)
        return ans