class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = sum(nums)
        presum = 0
        for i in range(len(nums)):
            if presum * 2 + nums[i] == sums:
                return i
            presum += nums[i]

        return -1