class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = sum(nums)
        presum = 0
        for i in range(len(nums)):
            if presum == sums - presum- nums[i]:
                return i
            presum += nums[i]
        return -1