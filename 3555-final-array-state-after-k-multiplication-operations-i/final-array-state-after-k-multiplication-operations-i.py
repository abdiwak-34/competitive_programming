class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for ind, val in enumerate(nums):
            heapq.heappush(heap, (val,ind))
        while k > 0:
            value, indx = heapq.heappop(heap)
            value *= multiplier
            heapq.heappush(heap,(value,indx))
            k -= 1
        while heap:
            val, ind = heapq.heappop(heap)
            nums[ind] = val
        return nums