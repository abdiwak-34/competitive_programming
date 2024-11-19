class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum = nums[0]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            minimum = min(minimum,nums[i])
        if minimum >= 0:
            return 1
        return 1- minimum