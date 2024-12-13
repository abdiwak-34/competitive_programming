class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        heap = []
        score = 0
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        while heap:
            num, indx = heapq.heappop(heap)
            if indx in marked:
                continue
            score += num
            marked.add(indx)
            marked.add(indx+1)
            marked.add(indx-1)
        return score