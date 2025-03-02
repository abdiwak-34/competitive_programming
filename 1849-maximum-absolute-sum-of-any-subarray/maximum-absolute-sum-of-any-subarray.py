class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        positive = negative = maximum = 0
        for i in range(len(nums)):
            positive += nums[i]
            positive = max(positive, 0)

            negative += nums[i]
            negative = min(negative, 0)
            maximum = max(maximum, positive, -negative)

        return maximum