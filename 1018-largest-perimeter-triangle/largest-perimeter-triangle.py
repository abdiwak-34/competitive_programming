class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maximum = 0
        nums.sort()
        for i in range(2, len(nums)):
            if nums[i-2] +nums[i-1] > nums[i]:
                maximum = sum([nums[i-2],nums[i-1],nums[i]])
        return maximum