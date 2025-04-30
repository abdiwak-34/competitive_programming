from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for key, val in count.items():
            heappush(heap, (-val, key))
        
        ans = []
        for i in range(k):
            _, element = heappop(heap)
            ans.append(element)
        return ans