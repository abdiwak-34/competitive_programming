class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        sums = 0
        for i in range(len(nums)):
            sums = max(sums, 0) + nums[i]
            maximum = max(maximum, sums)
        return maximum