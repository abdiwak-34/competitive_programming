from heapq import heapify, heappush, heappop
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        while len(nums) > 1:
            x = heappop(nums)
            if x >= k:
                return count
            y = heappop(nums)
            new = (min(x, y) * 2 + max(x, y))
            heappush(nums, new)
            count += 1
        return count


