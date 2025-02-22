class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        request = [0] * len(nums)
        for start, end in requests:
            request[start] += 1
            if end+1 < len(nums):
                request[end+1] -= 1
        for i in range(1,len(nums)):
            request[i] += request[i-1]
        request.sort()
        nums.sort()
        total = 0
        for i in range(len(nums)):
            total += (request[i] * nums[i])
        return total % (10**9 + 7)