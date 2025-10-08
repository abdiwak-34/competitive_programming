class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum = 0
        maximum_sum = -float('inf')
        for i in range(len(nums)):
            if presum < 0:
                presum = nums[i]
            else:
                presum += nums[i]
            maximum_sum = max(maximum_sum, presum)
        
        return maximum_sum