import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = max(nums)
        m = abs(min(nums))
        count = [0] * (n+m+1)
        for num in nums:
            count[num+m] += 1
        target = 0
        for ind, val in enumerate(count):
            for i in range(val):
                nums[target] = ind - m
                target += 1
        return nums