class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maximum = 0
        nums.sort()
        sums = sum(nums[:2])
        for i in range(2, len(nums)):
            sums += nums[i]
            if nums[i-2] +nums[i-1] > nums[i]:
                maximum = sums
            sums -= nums[i-2]
        return maximum